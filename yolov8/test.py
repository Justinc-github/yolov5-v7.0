from ultralytics import YOLO
url = "rtsp://admin:yu20021014..@192.168.1.103/Streaming/Channels/1"
photo_url = "./数据集/dataset-pose/train/images/2218.jpg"
# 加载模型，确保只加载一次
model = YOLO("./runs/pose/train23/weights/best.pt")
results = model(photo_url, show=False, conf=0.4, save=True, device=0)
# # 打开摄像头
# cap = cv2.VideoCapture(url)
#
# # 准备FPS计算
# fps = 0.0
# start_time = time.perf_counter()
#
# while True:
#     # 按'q'退出
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
#     # 读取帧
#     ret, frame = cap.read()
#     if not ret:
#         break
#
#     # 计算处理开始时间
#     start = time.perf_counter()
#
#     # 进行模型推理
#     results = model(frame, show=False, conf=0.4, save=False, device=0)
#     if results:
#         annotated_frame = results[0].plot()
#
#     # 计算处理结束时间并计算FPS
#     end = time.perf_counter()
#     total_time = end - start
#     fps = 1 / total_time
#
#     # 绘制FPS
#     cv2.putText(annotated_frame, f"FPS:{int(fps)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
#
#     # 显示结果
#     cv2.imshow("test", annotated_frame)
#
# # 释放资源
# cap.release()
# cv2.destroyAllWindows()
