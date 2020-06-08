import numpy as np

def PreProcessImage(img):
    img_data = np.array(img)
    img_data = np.transpose(img_data, [2, 0, 1])
    img_data = np.expand_dims(img_data, 0)
    mean_vec = np.array([0.485, 0.456, 0.406])
    stddev_vec = np.array([0.229, 0.224, 0.225])
    norm_img_data = np.zeros(img_data.shape).astype('float32')
    for i in range(img_data.shape[1]):
        norm_img_data[:,i,:,:] = (img_data[:,i,:,:]/255 - mean_vec[i]) / stddev_vec[i]
    return norm_img_data


def PostProcess(result,size):
    
    classes = [line.rstrip('\n') for line in open('utils/coco_classes.txt')]
    
    bboxes = []
    for box in result[0][0]: bboxes.append(box)
    labels = []
    for label in result[1][0]: labels.append(label)    
    scores = []
    for score in result[2][0]: scores.append(score)
    
    scores, bboxes, labels = FormatResults(scores,bboxes,labels,classes,size)
    result = []
    for i in range( min(len(labels), 10)):
        val = [ labels[i], bboxes[i] ]
        result.append(val)
    res = {"result" : result}
    return res
    
def FormatResults(scores,bboxes,labels,classes,size):
    prev_score = scores[0]
    confidence_scores = []
    final_labels = []
    final_bboxes =[]
    
    for score in scores:
        if score >= prev_score*0.6 and score>=0.35 :
            prev_score = score
            confidence_scores.append(score*100)
        else:
            break
        
    for i in range(len(confidence_scores)):
        final_labels.append(classes[labels[i]-1])
        bbox = [ bboxes[i][0]*size[0], bboxes[i][1]*size[1], bboxes[i][2]*size[0], bboxes[i][3]*size[1] ]
        final_bboxes.append(bbox)    
    
    return confidence_scores, final_bboxes, final_labels