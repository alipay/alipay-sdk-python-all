#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExtendFieldInfo import ExtendFieldInfo


class AlipayIserviceItaskProcessDetailModifyModel(object):

    def __init__(self):
        self._app_name = None
        self._attachment = None
        self._exapp_name = None
        self._exsystem_department_id = None
        self._exsystem_department_name = None
        self._exsystem_operate = None
        self._exsystem_operator_comment = None
        self._exsystem_operator_id = None
        self._exsystem_operator_name = None
        self._extend_field_infos = None
        self._process_no = None
        self._process_template_code = None
        self._process_unique_id = None

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
    def exsystem_operate(self):
        return self._exsystem_operate

    @exsystem_operate.setter
    def exsystem_operate(self, value):
        self._exsystem_operate = value
    @property
    def exsystem_operator_comment(self):
        return self._exsystem_operator_comment

    @exsystem_operator_comment.setter
    def exsystem_operator_comment(self, value):
        self._exsystem_operator_comment = value
    @property
    def exsystem_operator_id(self):
        return self._exsystem_operator_id

    @exsystem_operator_id.setter
    def exsystem_operator_id(self, value):
        self._exsystem_operator_id = value
    @property
    def exsystem_operator_name(self):
        return self._exsystem_operator_name

    @exsystem_operator_name.setter
    def exsystem_operator_name(self, value):
        self._exsystem_operator_name = value
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
    @property
    def process_unique_id(self):
        return self._process_unique_id

    @process_unique_id.setter
    def process_unique_id(self, value):
        self._process_unique_id = value


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
        if self.exsystem_operate:
            if hasattr(self.exsystem_operate, 'to_alipay_dict'):
                params['exsystem_operate'] = self.exsystem_operate.to_alipay_dict()
            else:
                params['exsystem_operate'] = self.exsystem_operate
        if self.exsystem_operator_comment:
            if hasattr(self.exsystem_operator_comment, 'to_alipay_dict'):
                params['exsystem_operator_comment'] = self.exsystem_operator_comment.to_alipay_dict()
            else:
                params['exsystem_operator_comment'] = self.exsystem_operator_comment
        if self.exsystem_operator_id:
            if hasattr(self.exsystem_operator_id, 'to_alipay_dict'):
                params['exsystem_operator_id'] = self.exsystem_operator_id.to_alipay_dict()
            else:
                params['exsystem_operator_id'] = self.exsystem_operator_id
        if self.exsystem_operator_name:
            if hasattr(self.exsystem_operator_name, 'to_alipay_dict'):
                params['exsystem_operator_name'] = self.exsystem_operator_name.to_alipay_dict()
            else:
                params['exsystem_operator_name'] = self.exsystem_operator_name
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
        if self.process_unique_id:
            if hasattr(self.process_unique_id, 'to_alipay_dict'):
                params['process_unique_id'] = self.process_unique_id.to_alipay_dict()
            else:
                params['process_unique_id'] = self.process_unique_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceItaskProcessDetailModifyModel()
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'attachment' in d:
            o.attachment = d['attachment']
        if 'exapp_name' in d:
            o.exapp_name = d['exapp_name']
        if 'exsystem_department_id' in d:
            o.exsystem_department_id = d['exsystem_department_id']
        if 'exsystem_department_name' in d:
            o.exsystem_department_name = d['exsystem_department_name']
        if 'exsystem_operate' in d:
            o.exsystem_operate = d['exsystem_operate']
        if 'exsystem_operator_comment' in d:
            o.exsystem_operator_comment = d['exsystem_operator_comment']
        if 'exsystem_operator_id' in d:
            o.exsystem_operator_id = d['exsystem_operator_id']
        if 'exsystem_operator_name' in d:
            o.exsystem_operator_name = d['exsystem_operator_name']
        if 'extend_field_infos' in d:
            o.extend_field_infos = d['extend_field_infos']
        if 'process_no' in d:
            o.process_no = d['process_no']
        if 'process_template_code' in d:
            o.process_template_code = d['process_template_code']
        if 'process_unique_id' in d:
            o.process_unique_id = d['process_unique_id']
        return o


