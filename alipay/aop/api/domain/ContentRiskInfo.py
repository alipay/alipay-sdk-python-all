#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RiskInfo import RiskInfo
from alipay.aop.api.domain.SubContentRiskInfo import SubContentRiskInfo


class ContentRiskInfo(object):

    def __init__(self):
        self._content_file_type = None
        self._ext = None
        self._ocr_info = None
        self._out_content_id = None
        self._risk_info_list = None
        self._sub_content_risk_info_list = None

    @property
    def content_file_type(self):
        return self._content_file_type

    @content_file_type.setter
    def content_file_type(self, value):
        self._content_file_type = value
    @property
    def ext(self):
        return self._ext

    @ext.setter
    def ext(self, value):
        self._ext = value
    @property
    def ocr_info(self):
        return self._ocr_info

    @ocr_info.setter
    def ocr_info(self, value):
        self._ocr_info = value
    @property
    def out_content_id(self):
        return self._out_content_id

    @out_content_id.setter
    def out_content_id(self, value):
        self._out_content_id = value
    @property
    def risk_info_list(self):
        return self._risk_info_list

    @risk_info_list.setter
    def risk_info_list(self, value):
        if isinstance(value, list):
            self._risk_info_list = list()
            for i in value:
                if isinstance(i, RiskInfo):
                    self._risk_info_list.append(i)
                else:
                    self._risk_info_list.append(RiskInfo.from_alipay_dict(i))
    @property
    def sub_content_risk_info_list(self):
        return self._sub_content_risk_info_list

    @sub_content_risk_info_list.setter
    def sub_content_risk_info_list(self, value):
        if isinstance(value, list):
            self._sub_content_risk_info_list = list()
            for i in value:
                if isinstance(i, SubContentRiskInfo):
                    self._sub_content_risk_info_list.append(i)
                else:
                    self._sub_content_risk_info_list.append(SubContentRiskInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.content_file_type:
            if hasattr(self.content_file_type, 'to_alipay_dict'):
                params['content_file_type'] = self.content_file_type.to_alipay_dict()
            else:
                params['content_file_type'] = self.content_file_type
        if self.ext:
            if hasattr(self.ext, 'to_alipay_dict'):
                params['ext'] = self.ext.to_alipay_dict()
            else:
                params['ext'] = self.ext
        if self.ocr_info:
            if hasattr(self.ocr_info, 'to_alipay_dict'):
                params['ocr_info'] = self.ocr_info.to_alipay_dict()
            else:
                params['ocr_info'] = self.ocr_info
        if self.out_content_id:
            if hasattr(self.out_content_id, 'to_alipay_dict'):
                params['out_content_id'] = self.out_content_id.to_alipay_dict()
            else:
                params['out_content_id'] = self.out_content_id
        if self.risk_info_list:
            if isinstance(self.risk_info_list, list):
                for i in range(0, len(self.risk_info_list)):
                    element = self.risk_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.risk_info_list[i] = element.to_alipay_dict()
            if hasattr(self.risk_info_list, 'to_alipay_dict'):
                params['risk_info_list'] = self.risk_info_list.to_alipay_dict()
            else:
                params['risk_info_list'] = self.risk_info_list
        if self.sub_content_risk_info_list:
            if isinstance(self.sub_content_risk_info_list, list):
                for i in range(0, len(self.sub_content_risk_info_list)):
                    element = self.sub_content_risk_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sub_content_risk_info_list[i] = element.to_alipay_dict()
            if hasattr(self.sub_content_risk_info_list, 'to_alipay_dict'):
                params['sub_content_risk_info_list'] = self.sub_content_risk_info_list.to_alipay_dict()
            else:
                params['sub_content_risk_info_list'] = self.sub_content_risk_info_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContentRiskInfo()
        if 'content_file_type' in d:
            o.content_file_type = d['content_file_type']
        if 'ext' in d:
            o.ext = d['ext']
        if 'ocr_info' in d:
            o.ocr_info = d['ocr_info']
        if 'out_content_id' in d:
            o.out_content_id = d['out_content_id']
        if 'risk_info_list' in d:
            o.risk_info_list = d['risk_info_list']
        if 'sub_content_risk_info_list' in d:
            o.sub_content_risk_info_list = d['sub_content_risk_info_list']
        return o


