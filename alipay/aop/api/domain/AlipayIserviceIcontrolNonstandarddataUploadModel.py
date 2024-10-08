#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceIcontrolNonstandarddataUploadModel(object):

    def __init__(self):
        self._content = None
        self._nebula_id = None
        self._out_biz_code = None
        self._tnt_inst_id = None
        self._type = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def nebula_id(self):
        return self._nebula_id

    @nebula_id.setter
    def nebula_id(self, value):
        self._nebula_id = value
    @property
    def out_biz_code(self):
        return self._out_biz_code

    @out_biz_code.setter
    def out_biz_code(self, value):
        self._out_biz_code = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.nebula_id:
            if hasattr(self.nebula_id, 'to_alipay_dict'):
                params['nebula_id'] = self.nebula_id.to_alipay_dict()
            else:
                params['nebula_id'] = self.nebula_id
        if self.out_biz_code:
            if hasattr(self.out_biz_code, 'to_alipay_dict'):
                params['out_biz_code'] = self.out_biz_code.to_alipay_dict()
            else:
                params['out_biz_code'] = self.out_biz_code
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceIcontrolNonstandarddataUploadModel()
        if 'content' in d:
            o.content = d['content']
        if 'nebula_id' in d:
            o.nebula_id = d['nebula_id']
        if 'out_biz_code' in d:
            o.out_biz_code = d['out_biz_code']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        if 'type' in d:
            o.type = d['type']
        return o


