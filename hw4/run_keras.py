import numpy as np
import click
import time
import os
import tensorflow as tf
from tensorflow.python.framework.convert_to_constants import (
    convert_variables_to_constants_v2,
)

def measure(func, args, repeats=50):
    res = []
    for _ in range(repeats):
        start = time.time()
        func(args)
        end = time.time()
        res.append((end - start) * 1000.)
    return np.mean(res), np.std(res)


def _load_keras_model(module, name, seq_len, batch_size):
    model = module.from_pretrained(name)
    dummy_input = tf.keras.Input(
        shape=[seq_len], batch_size=batch_size, dtype="int32")
    dummy_out = model(dummy_input)  # Propagate shapes through the keras model.
    return model

def keras_to_graphdef(model, batch_size, seq_len):
    model_func = tf.function(lambda x: model(x))
    input_dict = model._saved_model_inputs_spec
    input_spec = input_dict[list(input_dict.keys())[0]]
    model_func = model_func.get_concrete_function(
        tf.TensorSpec([batch_size, seq_len], input_spec.dtype)
    )
    frozen_func = convert_variables_to_constants_v2(model_func)
    return frozen_func.graph.as_graph_def()

def get_huggingface_model(name, batch_size, seq_len):
    import transformers
    module = getattr(transformers, "TFBertForSequenceClassification")
    model = _load_keras_model(
        module, name=name, batch_size=batch_size, seq_len=seq_len)
    return model


@click.command()
@click.option("==model-name", default='bert-base-uncased')
@click.option('--device', required=True, help="device will be used, [cpu] or [gpu]")
def main(model_name, device):
    if device == "cpu":
        tf.config.experimental.set_visible_devices([], 'GPU')
    elif device == "gpu":
        tf.device('/gpu:0')
    else:
        raise Exception("Unknown devices")    
    batch_size = 1
    seq_len = 128
    model = get_huggingface_model(model_name,
                                           batch_size,
                                           seq_len)
    def run_keras(args):
        assert len(args) == 2
        model = args[0]
        np_input = args[1]
        _ = model(np_input)
    
    run_args = [
        model,
        np.random.randint(0, 10000, size=[batch_size, seq_len]).astype(np.int32)
    ]

    mean, std = measure(run_keras, run_args)
    print("[Keras] Mean Inference time (std dev) on {device}: {mean_time} ms ({std} ms)".format(
        device=device, mean_time=mean, std=std
    ))

if __name__ == "__main__":
    main()