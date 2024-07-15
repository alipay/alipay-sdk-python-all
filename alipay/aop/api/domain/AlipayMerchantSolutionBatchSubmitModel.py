#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AlipaySolutionFile import AlipaySolutionFile


class AlipayMerchantSolutionBatchSubmitModel(object):

    def __init__(self):
        self._file_info = None
        self._out_batch_no = None
        self._scene_code = None
        self._solution_code = None

    @property
    def file_info(self):
        return self._file_info

    @file_info.setter
    def file_info(self, value):
        if isinstance(value, list):
            self._file_info = list()
            for i in value:
                if isinstance(i, AlipaySolutionFile):
                    self._file_info.append(i)
                else:
                    self._file_info.append(AlipaySolutionFile.from_alipay_dict(i))
    @property
    def out_batch_no(self):
        return self._out_batch_no

    @out_batch_no.setter
    def out_batch_no(self, value):
        self._out_batch_no = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def solution_code(self):
        return self._solution_code

    @solution_code.setter
    def solution_code(self, value):
        self._solution_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.file_info:
            if isinstance(self.file_info, list):
                for i in range(0, len(self.file_info)):
                    element = self.file_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.file_info[i] = element.to_alipay_dict()
            if hasattr(self.file_info, 'to_alipay_dict'):
                params['file_info'] = self.file_info.to_alipay_dict()
            else:
                params['file_info'] = self.file_info
        if self.out_batch_no:
            if hasattr(self.out_batch_no, 'to_alipay_dict'):
                params['out_batch_no'] = self.out_batch_no.to_alipay_dict()
            else:
                params['out_batch_no'] = self.out_batch_no
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.solution_code:
            if hasattr(self.solution_code, 'to_alipay_dict'):
                params['solution_code'] = self.solution_code.to_alipay_dict()
            else:
                params['solution_code'] = self.solution_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantSolutionBatchSubmitModel()
        if 'file_info' in d:
            o.file_info = d['file_info']
        if 'out_batch_no' in d:
            o.out_batch_no = d['out_batch_no']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'solution_code' in d:
            o.solution_code = d['solution_code']
        return o


