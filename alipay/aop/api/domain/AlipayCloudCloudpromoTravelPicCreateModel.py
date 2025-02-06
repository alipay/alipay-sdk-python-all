#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudpromoTravelPicCreateModel(object):

    def __init__(self):
        self._pic_1 = None
        self._pic_2 = None
        self._pic_3 = None
        self._pic_4 = None
        self._template_id = None
        self._text_1 = None
        self._text_2 = None
        self._text_3 = None
        self._text_4 = None

    @property
    def pic_1(self):
        return self._pic_1

    @pic_1.setter
    def pic_1(self, value):
        self._pic_1 = value
    @property
    def pic_2(self):
        return self._pic_2

    @pic_2.setter
    def pic_2(self, value):
        self._pic_2 = value
    @property
    def pic_3(self):
        return self._pic_3

    @pic_3.setter
    def pic_3(self, value):
        self._pic_3 = value
    @property
    def pic_4(self):
        return self._pic_4

    @pic_4.setter
    def pic_4(self, value):
        self._pic_4 = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def text_1(self):
        return self._text_1

    @text_1.setter
    def text_1(self, value):
        self._text_1 = value
    @property
    def text_2(self):
        return self._text_2

    @text_2.setter
    def text_2(self, value):
        self._text_2 = value
    @property
    def text_3(self):
        return self._text_3

    @text_3.setter
    def text_3(self, value):
        self._text_3 = value
    @property
    def text_4(self):
        return self._text_4

    @text_4.setter
    def text_4(self, value):
        self._text_4 = value


    def to_alipay_dict(self):
        params = dict()
        if self.pic_1:
            if hasattr(self.pic_1, 'to_alipay_dict'):
                params['pic_1'] = self.pic_1.to_alipay_dict()
            else:
                params['pic_1'] = self.pic_1
        if self.pic_2:
            if hasattr(self.pic_2, 'to_alipay_dict'):
                params['pic_2'] = self.pic_2.to_alipay_dict()
            else:
                params['pic_2'] = self.pic_2
        if self.pic_3:
            if hasattr(self.pic_3, 'to_alipay_dict'):
                params['pic_3'] = self.pic_3.to_alipay_dict()
            else:
                params['pic_3'] = self.pic_3
        if self.pic_4:
            if hasattr(self.pic_4, 'to_alipay_dict'):
                params['pic_4'] = self.pic_4.to_alipay_dict()
            else:
                params['pic_4'] = self.pic_4
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.text_1:
            if hasattr(self.text_1, 'to_alipay_dict'):
                params['text_1'] = self.text_1.to_alipay_dict()
            else:
                params['text_1'] = self.text_1
        if self.text_2:
            if hasattr(self.text_2, 'to_alipay_dict'):
                params['text_2'] = self.text_2.to_alipay_dict()
            else:
                params['text_2'] = self.text_2
        if self.text_3:
            if hasattr(self.text_3, 'to_alipay_dict'):
                params['text_3'] = self.text_3.to_alipay_dict()
            else:
                params['text_3'] = self.text_3
        if self.text_4:
            if hasattr(self.text_4, 'to_alipay_dict'):
                params['text_4'] = self.text_4.to_alipay_dict()
            else:
                params['text_4'] = self.text_4
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudpromoTravelPicCreateModel()
        if 'pic_1' in d:
            o.pic_1 = d['pic_1']
        if 'pic_2' in d:
            o.pic_2 = d['pic_2']
        if 'pic_3' in d:
            o.pic_3 = d['pic_3']
        if 'pic_4' in d:
            o.pic_4 = d['pic_4']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'text_1' in d:
            o.text_1 = d['text_1']
        if 'text_2' in d:
            o.text_2 = d['text_2']
        if 'text_3' in d:
            o.text_3 = d['text_3']
        if 'text_4' in d:
            o.text_4 = d['text_4']
        return o


