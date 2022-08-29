#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RiskInfoDetail(object):

    def __init__(self):
        self._hit_word = None
        self._hit_word_index = None
        self._new_picture_frame = None
        self._picture_frame = None

    @property
    def hit_word(self):
        return self._hit_word

    @hit_word.setter
    def hit_word(self, value):
        self._hit_word = value
    @property
    def hit_word_index(self):
        return self._hit_word_index

    @hit_word_index.setter
    def hit_word_index(self, value):
        self._hit_word_index = value
    @property
    def new_picture_frame(self):
        return self._new_picture_frame

    @new_picture_frame.setter
    def new_picture_frame(self, value):
        self._new_picture_frame = value
    @property
    def picture_frame(self):
        return self._picture_frame

    @picture_frame.setter
    def picture_frame(self, value):
        self._picture_frame = value


    def to_alipay_dict(self):
        params = dict()
        if self.hit_word:
            if hasattr(self.hit_word, 'to_alipay_dict'):
                params['hit_word'] = self.hit_word.to_alipay_dict()
            else:
                params['hit_word'] = self.hit_word
        if self.hit_word_index:
            if hasattr(self.hit_word_index, 'to_alipay_dict'):
                params['hit_word_index'] = self.hit_word_index.to_alipay_dict()
            else:
                params['hit_word_index'] = self.hit_word_index
        if self.new_picture_frame:
            if hasattr(self.new_picture_frame, 'to_alipay_dict'):
                params['new_picture_frame'] = self.new_picture_frame.to_alipay_dict()
            else:
                params['new_picture_frame'] = self.new_picture_frame
        if self.picture_frame:
            if hasattr(self.picture_frame, 'to_alipay_dict'):
                params['picture_frame'] = self.picture_frame.to_alipay_dict()
            else:
                params['picture_frame'] = self.picture_frame
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RiskInfoDetail()
        if 'hit_word' in d:
            o.hit_word = d['hit_word']
        if 'hit_word_index' in d:
            o.hit_word_index = d['hit_word_index']
        if 'new_picture_frame' in d:
            o.new_picture_frame = d['new_picture_frame']
        if 'picture_frame' in d:
            o.picture_frame = d['picture_frame']
        return o


