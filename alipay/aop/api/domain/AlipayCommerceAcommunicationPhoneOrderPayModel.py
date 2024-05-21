#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceAcommunicationPhoneOrderPayModel(object):

    def __init__(self):
        self._face = None
        self._mobile = None
        self._out_biz_no = None
        self._price_ceiling = None
        self._related_biz_no = None
        self._scene = None
        self._start_time = None
        self._step_count = None
        self._step_number = None
        self._sub_source = None

    @property
    def face(self):
        return self._face

    @face.setter
    def face(self, value):
        self._face = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def price_ceiling(self):
        return self._price_ceiling

    @price_ceiling.setter
    def price_ceiling(self, value):
        self._price_ceiling = value
    @property
    def related_biz_no(self):
        return self._related_biz_no

    @related_biz_no.setter
    def related_biz_no(self, value):
        self._related_biz_no = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def step_count(self):
        return self._step_count

    @step_count.setter
    def step_count(self, value):
        self._step_count = value
    @property
    def step_number(self):
        return self._step_number

    @step_number.setter
    def step_number(self, value):
        self._step_number = value
    @property
    def sub_source(self):
        return self._sub_source

    @sub_source.setter
    def sub_source(self, value):
        self._sub_source = value


    def to_alipay_dict(self):
        params = dict()
        if self.face:
            if hasattr(self.face, 'to_alipay_dict'):
                params['face'] = self.face.to_alipay_dict()
            else:
                params['face'] = self.face
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.price_ceiling:
            if hasattr(self.price_ceiling, 'to_alipay_dict'):
                params['price_ceiling'] = self.price_ceiling.to_alipay_dict()
            else:
                params['price_ceiling'] = self.price_ceiling
        if self.related_biz_no:
            if hasattr(self.related_biz_no, 'to_alipay_dict'):
                params['related_biz_no'] = self.related_biz_no.to_alipay_dict()
            else:
                params['related_biz_no'] = self.related_biz_no
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.step_count:
            if hasattr(self.step_count, 'to_alipay_dict'):
                params['step_count'] = self.step_count.to_alipay_dict()
            else:
                params['step_count'] = self.step_count
        if self.step_number:
            if hasattr(self.step_number, 'to_alipay_dict'):
                params['step_number'] = self.step_number.to_alipay_dict()
            else:
                params['step_number'] = self.step_number
        if self.sub_source:
            if hasattr(self.sub_source, 'to_alipay_dict'):
                params['sub_source'] = self.sub_source.to_alipay_dict()
            else:
                params['sub_source'] = self.sub_source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceAcommunicationPhoneOrderPayModel()
        if 'face' in d:
            o.face = d['face']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'price_ceiling' in d:
            o.price_ceiling = d['price_ceiling']
        if 'related_biz_no' in d:
            o.related_biz_no = d['related_biz_no']
        if 'scene' in d:
            o.scene = d['scene']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'step_count' in d:
            o.step_count = d['step_count']
        if 'step_number' in d:
            o.step_number = d['step_number']
        if 'sub_source' in d:
            o.sub_source = d['sub_source']
        return o


