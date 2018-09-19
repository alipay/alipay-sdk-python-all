#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExtendFieldInfo import ExtendFieldInfo


class AlipayIserviceItaskProcessDetailCreateModel(object):

    def __init__(self):
        self._app_name = None
        self._attachment = None
        self._exapp_name = None
        self._excreator_id = None
        self._excreator_name = None
        self._exsystem_department_id = None
        self._exsystem_department_name = None
        self._extend_field_infos = None
        self._process_no = None
        self._process_template_code = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def attachment(self):
        return self._attachment

    @attachment.setter
    def attachment(self, value):
        self._attachment = value
    @property
    def exapp_name(self):
        return self._exapp_name

    @exapp_name.setter
    def exapp_name(self, value):
        self._exapp_name = value
    @property
    def excreator_id(self):
        return self._excreator_id

    @excreator_id.setter
    def excreator_id(self, value):
        self._excreator_id = value
    @property
    def excreator_name(self):
        return self._excreator_name

    @excreator_name.setter
    def excreator_name(self, value):
        self._excreator_name = value
    @property
    def exsystem_department_id(self):
        return self._exsystem_department_id

    @exsystem_department_id.setter
    def exsystem_department_id(self, value):
        self._exsystem_department_id = value
    @property
    def exsystem_department_name(self):
        return self._exsystem_department_name

    @exsystem_department_name.setter
    def exsystem_department_name(self, value):
        self._exsystem_department_name = value
    @property
    def extend_field_infos(self):
        return self._extend_field_infos

    @extend_field_infos.setter
    def extend_field_infos(self, value):
        if isinstance(value, list):
            self._extend_field_infos = list()
            for i in value:
                if isinstance(i, ExtendFieldInfo):
                    self._extend_field_infos.append(i)
                else:
                    self._extend_field_infos.append(ExtendFieldInfo.from_alipay_dict(i))
    @property
    def process_no(self):
        return self._process_no

    @process_no.setter
    def process_no(self, value):
        self._process_no = value
    @property
    def process_template_code(self):
        return self._process_template_code

    @process_template_code.setter
    def process_template_code(self, value):
        self._process_template_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.attachment:
            if hasattr(self.attachment, 'to_alipay_dict'):
                params['attachment'] = self.attachment.to_alipay_dict()
            else:
                params['attachment'] = self.attachment
        if self.exapp_name:
            if hasattr(self.exapp_name, 'to_alipay_dict'):
                params['exapp_name'] = self.exapp_name.to_alipay_dict()
            else:
                params['exapp_name'] = self.exapp_name
        if self.excreator_id:
            if hasattr(self.excreator_id, 'to_alipay_dict'):
                params['excreator_id'] = self.excreator_id.to_alipay_dict()
            else:
                params['excreator_id'] = self.excreator_id
        if self.excreator_name:
            if hasattr(self.excreator_name, 'to_alipay_dict'):
                params['excreator_name'] = self.excreator_name.to_alipay_dict()
            else:
                params['excreator_name'] = self.excreator_name
        if self.exsystem_department_id:
            if hasattr(self.exsystem_department_id, 'to_alipay_dict'):
                params['exsystem_department_id'] = self.exsystem_department_id.to_alipay_dict()
            else:
                params['exsystem_department_id'] = self.exsystem_department_id
        if self.exsystem_department_name:
            if hasattr(self.exsystem_department_name, 'to_alipay_dict'):
                params['exsystem_department_name'] = self.exsystem_department_name.to_alipay_dict()
            else:
                params['exsystem_department_name'] = self.exsystem_department_name
        if self.extend_field_infos:
            if isinstance(self.extend_field_infos, list):
                for i in range(0, len(self.extend_field_infos)):
                    element = self.extend_field_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.extend_field_infos[i] = element.to_alipay_dict()
            if hasattr(self.extend_field_infos, 'to_alipay_dict'):
                params['extend_field_infos'] = self.extend_field_infos.to_alipay_dict()
            else:
                params['extend_field_infos'] = self.extend_field_infos
        if self.process_no:
            if hasattr(self.process_no, 'to_alipay_dict'):
                params['process_no'] = self.process_no.to_alipay_dict()
            else:
                params['process_no'] = self.process_no
        if self.process_template_code:
            if hasattr(self.process_template_code, 'to_alipay_dict'):
                params['process_template_code'] = self.process_template_code.to_alipay_dict()
            else:
                params['process_template_code'] = self.process_template_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceItaskProcessDetailCreateModel()
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'attachment' in d:
            o.attachment = d['attachment']
        if 'exapp_name' in d:
            o.exapp_name = d['exapp_name']
        if 'excreator_id' in d:
            o.excreator_id = d['excreator_id']
        if 'excreator_name' in d:
            o.excreator_name = d['excreator_name']
        if 'exsystem_department_id' in d:
            o.exsystem_department_id = d['exsystem_department_id']
        if 'exsystem_department_name' in d:
            o.exsystem_department_name = d['exsystem_department_name']
        if 'extend_field_infos' in d:
            o.extend_field_infos = d['extend_field_infos']
        if 'process_no' in d:
            o.process_no = d['process_no']
        if 'process_template_code' in d:
            o.process_template_code = d['process_template_code']
        return o


