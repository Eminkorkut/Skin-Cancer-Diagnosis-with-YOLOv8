from ultralytics import YOLO
import argparse
import cv2
import os

def argsRun(
  weights='Models/basal.pt',
  source='1.jpg',
  patientNumber='0000000000',
  skinType='Basal'
):

  model = YOLO(weights[0])

  results = model.predict(source, conf=0.60, iou=0.1)
  result = results[0]

  if len(result.boxes) == 0:
      detectionObjectInf = "Cilt Kanseri Algılanamadı"
      if not os.path.exists(f"Logs/{patientNumber}"):
          os.makedirs(f"Logs/{patientNumber}")

      detectionObjectInf = f"Kanser Türü: Yok, Doğruluk Oranı: 0.00"
      savedTxtName = f"nullDetection.txt"
      detectNote = open(f"Logs/{patientNumber}/{savedTxtName}", "w")
      detectNote.write(detectionObjectInf)
      detectNote.close()

      cv2.imwrite(f"Logs/{patientNumber}/skinCancer.jpg", cv2.imread(source))

  else:
      detectionObjectInf = ""
      detectionObjectName = ""
      detectionObjectConf = 0.00

      for box in result.boxes:
          class_id = result.names[box.cls[0].item()]
          conf = round(box.conf[0].item(), 2)
          if conf >= detectionObjectConf:
              detectionObjectName = class_id
              detectionObjectConf = conf

      if os.path.exists(f"Logs/{patientNumber}"):
          print("Daha önce aynı hastan için kaydedilmiş bir çalışma var, veriler aynı dosyaya kaydedilecektir.")
      else:
          os.makedirs(f"Logs/{patientNumber}")
      
      if os.path.exists(f"Logs/{patientNumber}/{detectionObjectName}"):
          print("Daha önce aynı hastanın kanser tespiti için aynı kanser türünde yapılmış bir çalışma var, veriler yeniden kaydedilmeyecektir.")
      else:
          os.makedirs(f"Logs/{patientNumber}/{detectionObjectName}")
          
          detectionObjectInf = f"Kanser Türü: {detectionObjectName}, Doğruluk Oranı: {detectionObjectConf}"
          savedTxtName = f"{detectionObjectName}Detection.txt"
          detectNote = open(f"Logs/{patientNumber}/{detectionObjectName}/{savedTxtName}", "w")
          detectNote.write(detectionObjectInf)
          detectNote.close()   
          model = YOLO(weights[0])
          results = model.predict(source, save=True, conf=0.60, project=str(f"Logs/{patientNumber}/{detectionObjectName}/"), name=skinType, line_thickness=2, iou=0.1) 

  print(detectionObjectInf)

def parseOpt():
  parser = argparse.ArgumentParser()
  parser.add_argument('--weights', nargs='+', type=str, default='Models/basal.pt', help='model path or triton URL')
  parser.add_argument('--source', type=str, default='2.jpg', help='file/dir/URL/glob/screen/0(webcam)')
  parser.add_argument('--patientNumber', type=str, default='00000000000', help='Entry the patient number')
  parser.add_argument('--skinType', type=str, default='Basal', help='Entry the skin cancer type')
  return parser.parse_args()

if __name__ == '__main__':
  opt = parseOpt()
  argsRun(**vars(opt))
