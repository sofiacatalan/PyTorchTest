'''
Convert model to enable testing in C++ 
Following example from: https://pytorch.org/tutorials/advanced/cpp_export.html

Notes: 
    - this example script follows the tracing method to save the model. I tried 
      getting the annotation method (while that provided a saved model, 
      it doesn't run in the C++ example) 

Directions:
    - run this file to save the model
    - go to `./example-app/build`
    - run `cmake -DCMAKE_PREFIX_PATH=/absolute/path/to/libtorch ..`
    - run `cmake --build . --config Release`
    - run `./example-app ../../traced_resnet_model.pt`

'''

import torch 
import torchvision

# An instance of your model.
model = torchvision.models.resnet18()

# An example input you would normally provide to your model's forward() method.
example = torch.rand(1, 3, 224, 224)

# Use torch.jit.trace to generate a torch.jit.ScriptModule via tracing.
traced_script_module = torch.jit.trace(model, example)

traced_script_module.save("traced_resnet_model.pt")

# class MyModule(torch.nn.Module):
#     def __init__(self, N, M):
#         super(MyModule, self).__init__()
#         self.weight = torch.nn.Parameter(torch.rand(N, M))

#     def forward(self, input):
#         if input.sum() > 0:
#           output = self.weight.mv(input)
#         else:
#           output = self.weight + input
#         return output

# my_module = MyModule(10,20)
# sm = torch.jit.script(my_module)
# sm.save("traced_resnet_model.pt")