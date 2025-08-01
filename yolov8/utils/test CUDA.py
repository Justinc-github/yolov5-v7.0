import torch

#  检查PyTorch版本
print("PyTorch  Version:", torch.__version__)

#  检查CUDA是否可用
if torch.cuda.is_available():
    print("CUDA  is  available.")
    #  打印CUDA版本
    print("CUDA  Version:", torch.version.cuda)
else:
    print("CUDA  is  not  available.")

#  检查CUDA设备数量
print("Number  of  CUDA  devices:", torch.cuda.device_count())

#  如果你想获取更多关于CUDA设备的详细信息
if torch.cuda.device_count() > 0:
    for i in range(torch.cuda.device_count()):
        print(f"CUDA  Device  {i}:")
        print(f"    Name:  {torch.cuda.get_device_name(i)}")
        print(f"    Capability:  {torch.cuda.get_device_capability(i)}")

# import torch
#
# print(torch.cuda.is_available())  # 应该返回True
# print(torch.version.cuda)  # 应该显示CUDA版本，例如'12.1'
# print(torch.cuda.get_device_name(0))  # 应该显示显卡名称
#
# torch.backends.benchmark = True

