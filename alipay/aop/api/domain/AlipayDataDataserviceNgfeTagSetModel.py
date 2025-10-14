#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LabelUpdateExtInfo import LabelUpdateExtInfo
from alipay.aop.api.domain.LabelUpdateDetail import LabelUpdateDetail


class AlipayDataDataserviceNgfeTagSetModel(object):

    def __init__(self):
        self._app_name = None
        self._idempotent_id = None
        self._l_1_domain_code = None
        self._l_2_domain_code = None
        self._label_update_ext_info_list = None
        self._label_update_model_list = None
        self._object_id = None
        self._object_open_id = None
        self._scene = None
        self._source = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def idempotent_id(self):
        return self._idempotent_id

    @idempotent_id.setter
    def idempotent_id(self, value):
        self._idempotent_id = value
    @property
    def l_1_domain_code(self):
        return self._l_1_domain_code

    @l_1_domain_code.setter
    def l_1_domain_code(self, value):
        self._l_1_domain_code = value
    @property
    def l_2_domain_code(self):
        return self._l_2_domain_code

    @l_2_domain_code.setter
    def l_2_domain_code(self, value):
        self._l_2_domain_code = value
    @property
    def label_update_ext_info_list(self):
        return self._label_update_ext_info_list

    @label_update_ext_info_list.setter
    def label_update_ext_info_list(self, value):
        if isinstance(value, list):
            self._label_update_ext_info_list = list()
            for i in value:
                if isinstance(i, LabelUpdateExtInfo):
                    self._label_update_ext_info_list.append(i)
                else:
                    self._label_update_ext_info_list.append(LabelUpdateExtInfo.from_alipay_dict(i))
    @property
    def label_update_model_list(self):
        return self._label_update_model_list

    @label_update_model_list.setter
    def label_update_model_list(self, value):
        if isinstance(value, list):
            self._label_update_model_list = list()
            for i in value:
                if isinstance(i, LabelUpdateDetail):
                    self._label_update_model_list.append(i)
                else:
                    self._label_update_model_list.append(LabelUpdateDetail.from_alipay_dict(i))
    @property
    def object_id(self):
        return self._object_id

    @object_id.setter
    def object_id(self, value):
        self._object_id = value
    @property
    def object_open_id(self):
        return self._object_open_id

    @object_open_id.setter
    def object_open_id(self, value):
        self._object_open_id = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.idempotent_id:
            if hasattr(self.idempotent_id, 'to_alipay_dict'):
                params['idempotent_id'] = self.idempotent_id.to_alipay_dict()
            else:
                params['idempotent_id'] = self.idempotent_id
        if self.l_1_domain_code:
            if hasattr(self.l_1_domain_code, 'to_alipay_dict'):
                params['l_1_domain_code'] = self.l_1_domain_code.to_alipay_dict()
            else:
                params['l_1_domain_code'] = self.l_1_domain_code
        if self.l_2_domain_code:
            if hasattr(self.l_2_domain_code, 'to_alipay_dict'):
                params['l_2_domain_code'] = self.l_2_domain_code.to_alipay_dict()
            else:
                params['l_2_domain_code'] = self.l_2_domain_code
        if self.label_update_ext_info_list:
            if isinstance(self.label_update_ext_info_list, list):
                for i in range(0, len(self.label_update_ext_info_list)):
                    element = self.label_update_ext_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.label_update_ext_info_list[i] = element.to_alipay_dict()
            if hasattr(self.label_update_ext_info_list, 'to_alipay_dict'):
                params['label_update_ext_info_list'] = self.label_update_ext_info_list.to_alipay_dict()
            else:
                params['label_update_ext_info_list'] = self.label_update_ext_info_list
        if self.label_update_model_list:
            if isinstance(self.label_update_model_list, list):
                for i in range(0, len(self.label_update_model_list)):
                    element = self.label_update_model_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.label_update_model_list[i] = element.to_alipay_dict()
            if hasattr(self.label_update_model_list, 'to_alipay_dict'):
                params['label_update_model_list'] = self.label_update_model_list.to_alipay_dict()
            else:
                params['label_update_model_list'] = self.label_update_model_list
        if self.object_id:
            if hasattr(self.object_id, 'to_alipay_dict'):
                params['object_id'] = self.object_id.to_alipay_dict()
            else:
                params['object_id'] = self.object_id
        if self.object_open_id:
            if hasattr(self.object_open_id, 'to_alipay_dict'):
                params['object_open_id'] = self.object_open_id.to_alipay_dict()
            else:
                params['object_open_id'] = self.object_open_id
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceNgfeTagSetModel()
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'idempotent_id' in d:
            o.idempotent_id = d['idempotent_id']
        if 'l_1_domain_code' in d:
            o.l_1_domain_code = d['l_1_domain_code']
        if 'l_2_domain_code' in d:
            o.l_2_domain_code = d['l_2_domain_code']
        if 'label_update_ext_info_list' in d:
            o.label_update_ext_info_list = d['label_update_ext_info_list']
        if 'label_update_model_list' in d:
            o.label_update_model_list = d['label_update_model_list']
        if 'object_id' in d:
            o.object_id = d['object_id']
        if 'object_open_id' in d:
            o.object_open_id = d['object_open_id']
        if 'scene' in d:
            o.scene = d['scene']
        if 'source' in d:
            o.source = d['source']
        return o


