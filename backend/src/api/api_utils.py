import os
import importlib

def create_message_queue(options):
    module_name, class_name = options.mod_path.rsplit('.', 1)
    module = importlib.import_module(module_name)
    MessageQueue = getattr(module, class_name)
    return MessageQueue(options)

