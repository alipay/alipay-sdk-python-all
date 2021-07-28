#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PlanOperateContent import PlanOperateContent


class AlipayOpenMiniPlanOperateCreateModel(object):

    def __init__(self):
        self._app_belong = None
        self._gift_template_id = None
        self._oper_app_id = None
        self._pid = None
        self._plan_content = None
        self._plan_name = None
        self._scene = None
        self._service_list = None
        self._type = None

    @property
    def app_belong(self):
        return self._app_belong

    @app_belong.setter
    def app_belong(self, value):
        self._app_belong = value
    @property
    def gift_template_id(self):
        return self._gift_template_id

    @gift_template_id.setter
    def gift_template_id(self, value):
        self._gift_template_id = value
    @property
    def oper_app_id(self):
        return self._oper_app_id

    @oper_app_id.setter
    def oper_app_id(self, value):
        self._oper_app_id = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def plan_content(self):
        return self._plan_content

    @plan_content.setter
    def plan_content(self, value):
        if isinstance(value, list):
            self._plan_content = list()
            for i in value:
                if isinstance(i, PlanOperateContent):
                    self._plan_content.append(i)
                else:
                    self._plan_content.append(PlanOperateContent.from_alipay_dict(i))
    @property
    def plan_name(self):
        return self._plan_name

    @plan_name.setter
    def plan_name(self, value):
        self._plan_name = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def service_list(self):
        return self._service_list

    @service_list.setter
    def service_list(self, value):
        if isinstance(value, list):
            self._service_list = list()
            for i in value:
                self._service_list.append(i)
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_belong:
            if hasattr(self.app_belong, 'to_alipay_dict'):
                params['app_belong'] = self.app_belong.to_alipay_dict()
            else:
                params['app_belong'] = self.app_belong
        if self.gift_template_id:
            if hasattr(self.gift_template_id, 'to_alipay_dict'):
                params['gift_template_id'] = self.gift_template_id.to_alipay_dict()
            else:
                params['gift_template_id'] = self.gift_template_id
        if self.oper_app_id:
            if hasattr(self.oper_app_id, 'to_alipay_dict'):
                params['oper_app_id'] = self.oper_app_id.to_alipay_dict()
            else:
                params['oper_app_id'] = self.oper_app_id
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.plan_content:
            if isinstance(self.plan_content, list):
                for i in range(0, len(self.plan_content)):
                    element = self.plan_content[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.plan_content[i] = element.to_alipay_dict()
            if hasattr(self.plan_content, 'to_alipay_dict'):
                params['plan_content'] = self.plan_content.to_alipay_dict()
            else:
                params['plan_content'] = self.plan_content
        if self.plan_name:
            if hasattr(self.plan_name, 'to_alipay_dict'):
                params['plan_name'] = self.plan_name.to_alipay_dict()
            else:
                params['plan_name'] = self.plan_name
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.service_list:
            if isinstance(self.service_list, list):
                for i in range(0, len(self.service_list)):
                    element = self.service_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_list[i] = element.to_alipay_dict()
            if hasattr(self.service_list, 'to_alipay_dict'):
                params['service_list'] = self.service_list.to_alipay_dict()
            else:
                params['service_list'] = self.service_list
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
        o = AlipayOpenMiniPlanOperateCreateModel()
        if 'app_belong' in d:
            o.app_belong = d['app_belong']
        if 'gift_template_id' in d:
            o.gift_template_id = d['gift_template_id']
        if 'oper_app_id' in d:
            o.oper_app_id = d['oper_app_id']
        if 'pid' in d:
            o.pid = d['pid']
        if 'plan_content' in d:
            o.plan_content = d['plan_content']
        if 'plan_name' in d:
            o.plan_name = d['plan_name']
        if 'scene' in d:
            o.scene = d['scene']
        if 'service_list' in d:
            o.service_list = d['service_list']
        if 'type' in d:
            o.type = d['type']
        return o


