# -*- coding: utf-8 -*-
import pyltp
import os

LTP_DATA_DIR = r'D:\Tool\ltp_data_v3.4.0'  # ltp模型路径


def cut_words(words):
    # 分词模型
    seg_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')
    segmentor = pyltp.Segmentor()
    segmentor.load(seg_model_path)
    words = segmentor.segment(words)
    cws_str = "|".join(words)
    cws_array = cws_str.split("|")
    segmentor.release()
    return cws_array


def words_mark(array):
    # 词性标注
    pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')
    postagger = pyltp.Postagger()
    postagger.load(pos_model_path)
    postags = postagger.postag(array)
    pos_str = ' '.join(postags)
    pos_array = pos_str.split(" ")
    postagger.release()
    return pos_array


def get_target_array(words):
    target_pos = ['nh', 'n']
    target_array = []
    seg_array = cut_words(words)
    pos_array = words_mark(seg_array)
    for i in range(len(pos_array)):
        if pos_array[i] in target_pos:
            target_array.append(seg_array[i])
    target_array.append(seg_array[1])
    return target_array
