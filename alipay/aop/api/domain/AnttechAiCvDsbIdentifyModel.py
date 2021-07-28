#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DsbImageInfo import DsbImageInfo


class AnttechAiCvDsbIdentifyModel(object):

    def __init__(self):
        self._ant_estimate_no = None
        self._estimate_request_no = None
        self._image_info = None

    @property
    def ant_estimate_no(self):
        return self._ant_estimate_no

    @ant_estimate_no.setter
    def ant_estimate_no(self, value):
        self._ant_estimate_no = value
    @property
    def estimate_request_no(self):
        return self._estimate_request_no

    @estimate_request_no.setter
    def estimate_request_no(self, value):
        self._estimate_request_no = value
    @property
    def image_info(self):
        return self._image_info

    @image_info.setter
    def image_info(self, value):
        if isinstance(value, list):
            self._image_info = list()
            for i in value:
                if isinstance(i, DsbImageInfo):
                    self._image_info.append(i)
                else:
                    self._image_info.append(DsbImageInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.ant_estimate_no:
            if hasattr(self.ant_estimate_no, 'to_alipay_dict'):
                params['ant_estimate_no'] = self.ant_estimate_no.to_alipay_dict()
            else:
                params['ant_estimate_no'] = self.ant_estimate_no
        if self.estimate_request_no:
            if hasattr(self.estimate_request_no, 'to_alipay_dict'):
                params['estimate_request_no'] = self.estimate_request_no.to_alipay_dict()
            else:
                params['estimate_request_no'] = self.estimate_request_no
        if self.image_info:
            if isinstance(self.image_info, list):
                for i in range(0, len(self.image_info)):
                    element = self.image_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.image_info[i] = element.to_alipay_dict()
            if hasattr(self.image_info, 'to_alipay_dict'):
                params['image_info'] = self.image_info.to_alipay_dict()
            else:
                params['image_info'] = self.image_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechAiCvDsbIdentifyModel()
        if 'ant_estimate_no' in d:
            o.ant_estimate_no = d['ant_estimate_no']
        if 'estimate_request_no' in d:
            o.estimate_request_no = d['estimate_request_no']
        if 'image_info' in d:
            o.image_info = d['image_info']
        return o


