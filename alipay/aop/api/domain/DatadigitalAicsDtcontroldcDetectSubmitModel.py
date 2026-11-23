#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.QcContent import QcContent


class DatadigitalAicsDtcontroldcDetectSubmitModel(object):

    def __init__(self):
        self._app_name = None
        self._biz_id = None
        self._instance = None
        self._param = None
        self._qc_content = None
        self._qc_id = None
        self._tnt_inst_id = None
        self._trilateral_tnt_inst_id = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def instance(self):
        return self._instance

    @instance.setter
    def instance(self, value):
        self._instance = value
    @property
    def param(self):
        return self._param

    @param.setter
    def param(self, value):
        self._param = value
    @property
    def qc_content(self):
        return self._qc_content

    @qc_content.setter
    def qc_content(self, value):
        if isinstance(value, QcContent):
            self._qc_content = value
        else:
            self._qc_content = QcContent.from_alipay_dict(value)
    @property
    def qc_id(self):
        return self._qc_id

    @qc_id.setter
    def qc_id(self, value):
        self._qc_id = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value
    @property
    def trilateral_tnt_inst_id(self):
        return self._trilateral_tnt_inst_id

    @trilateral_tnt_inst_id.setter
    def trilateral_tnt_inst_id(self, value):
        self._trilateral_tnt_inst_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.instance:
            if hasattr(self.instance, 'to_alipay_dict'):
                params['instance'] = self.instance.to_alipay_dict()
            else:
                params['instance'] = self.instance
        if self.param:
            if hasattr(self.param, 'to_alipay_dict'):
                params['param'] = self.param.to_alipay_dict()
            else:
                params['param'] = self.param
        if self.qc_content:
            if hasattr(self.qc_content, 'to_alipay_dict'):
                params['qc_content'] = self.qc_content.to_alipay_dict()
            else:
                params['qc_content'] = self.qc_content
        if self.qc_id:
            if hasattr(self.qc_id, 'to_alipay_dict'):
                params['qc_id'] = self.qc_id.to_alipay_dict()
            else:
                params['qc_id'] = self.qc_id
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        if self.trilateral_tnt_inst_id:
            if hasattr(self.trilateral_tnt_inst_id, 'to_alipay_dict'):
                params['trilateral_tnt_inst_id'] = self.trilateral_tnt_inst_id.to_alipay_dict()
            else:
                params['trilateral_tnt_inst_id'] = self.trilateral_tnt_inst_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalAicsDtcontroldcDetectSubmitModel()
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'instance' in d:
            o.instance = d['instance']
        if 'param' in d:
            o.param = d['param']
        if 'qc_content' in d:
            o.qc_content = d['qc_content']
        if 'qc_id' in d:
            o.qc_id = d['qc_id']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        if 'trilateral_tnt_inst_id' in d:
            o.trilateral_tnt_inst_id = d['trilateral_tnt_inst_id']
        return o


