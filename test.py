from pyAudioAnalysis.audioSegmentation import mid_term_file_classification, labels_to_segments
# from pyAudioAnalysis.audioTrainTest import load_model

def test(audiofile_path):
    model_path = r"models/svm_male_female"
    model_type = "svm_rbf"
    plot_results = False

    labels, class_names, mt_step, class_probabilities = mid_term_file_classification(audiofile_path, model_path,
                                                                                     model_type, plot_results)

    print("labels: ", len(labels))
    # print "merged" segments (use labels_to_segments())
    # print("\nSegments:")
    segs, c, probs = labels_to_segments(labels, class_probabilities, mt_step)

    # print("segs: ", len(segs))
    print("prob test: ", len(probs))

    # for iS, seg in enumerate(segs):
    #     if probs[iS] > 0.6:
    #         print(f'segment {iS} {seg[0]} sec - {seg[1]} sec: {class_names[int(c[iS])]} pro: {probs[iS]}')
    # print("type(segs): ", type(segs))
    # print("type(probs): ", type(probs))

    return probs, segs.tolist(), class_names, c


# if __name__ == "__main__":
#
#     audiofile_path = r"/Users/taanhtuan/Desktop/workproject/basic_audio_analysis-master/data/test.mp3"
#     model_path = r"models/svm_male_female"
#     model_type = "svm_rbf"
#     plot_results = False
#
#     labels, class_names, mt_step, class_probabilities = mid_term_file_classification(audiofile_path, model_path,
#                                                              model_type, plot_results)
#
#     print("labels: ", len(labels))
#     # print "merged" segments (use labels_to_segments())
#     print("\nSegments:")
#     segs, c, probs = labels_to_segments(labels, class_probabilities, mt_step)
#
#     print("segs: ", len(segs))
#     print("prob: ", len(probs))
#
#     for iS, seg in enumerate(segs):
#         if probs[iS] > 0.58:
#             print(f'segment {iS} {seg[0]} sec - {seg[1]} sec: {class_names[int(c[iS])]} pro: {probs[iS]}')