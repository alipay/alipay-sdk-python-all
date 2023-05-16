#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ImgFile import ImgFile


class AlipaySecurityRiskComplaintProcessFinishModel(object):

    def __init__(self):
        self._id_list = None
        self._img_file_list = None
        self._process_code = None
        self._remark = None

    @property
    def id_list(self):
        return self._id_list

    @id_list.setter
    def id_list(self, value):
        if isinstance(value, list):
            self._id_list = list()
            for i in value:
                self._id_list.append(i)
    @property
    def img_file_list(self):
        return self._img_file_list

    @img_file_list.setter
    def img_file_list(self, value):
        if isinstance(value, list):
            self._img_file_list = list()
            for i in value:
                if isinstance(i, ImgFile):
                    self._img_file_list.append(i)
                else:
                    self._img_file_list.append(ImgFile.from_alipay_dict(i))
    @property
    def process_code(self):
        return self._process_code

    @process_code.setter
    def process_code(self, value):
        self._process_code = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value


    def to_alipay_dict(self):
        params = dict()
        if self.id_list:
            if isinstance(self.id_list, list):
                for i in range(0, len(self.id_list)):
                    element = self.id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.id_list[i] = element.to_alipay_dict()
            if hasattr(self.id_list, 'to_alipay_dict'):
                params['id_list'] = self.id_list.to_alipay_dict()
            else:
                params['id_list'] = self.id_list
        if self.img_file_list:
            if isinstance(self.img_file_list, list):
                for i in range(0, len(self.img_file_list)):
                    element = self.img_file_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.img_file_list[i] = element.to_alipay_dict()
            if hasattr(self.img_file_list, 'to_alipay_dict'):
                params['img_file_list'] = self.img_file_list.to_alipay_dict()
            else:
                params['img_file_list'] = self.img_file_list
        if self.process_code:
            if hasattr(self.process_code, 'to_alipay_dict'):
                params['process_code'] = self.process_code.to_alipay_dict()
            else:
                params['process_code'] = self.process_code
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityRiskComplaintProcessFinishModel()
        if 'id_list' in d:
            o.id_list = d['id_list']
        if 'img_file_list' in d:
            o.img_file_list = d['img_file_list']
        if 'process_code' in d:
            o.process_code = d['process_code']
        if 'remark' in d:
            o.remark = d['remark']
        return o


