#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ChangeBodyDTO import ChangeBodyDTO


class AlipayInsSceneOrderChangeConsultModel(object):

    def __init__(self):
        self._biz_id = None
        self._change_body_dto = None
        self._change_scene = None
        self._partner_org_id = None
        self._pre_order_id = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def change_body_dto(self):
        return self._change_body_dto

    @change_body_dto.setter
    def change_body_dto(self, value):
        if isinstance(value, ChangeBodyDTO):
            self._change_body_dto = value
        else:
            self._change_body_dto = ChangeBodyDTO.from_alipay_dict(value)
    @property
    def change_scene(self):
        return self._change_scene

    @change_scene.setter
    def change_scene(self, value):
        self._change_scene = value
    @property
    def partner_org_id(self):
        return self._partner_org_id

    @partner_org_id.setter
    def partner_org_id(self, value):
        self._partner_org_id = value
    @property
    def pre_order_id(self):
        return self._pre_order_id

    @pre_order_id.setter
    def pre_order_id(self, value):
        self._pre_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.change_body_dto:
            if hasattr(self.change_body_dto, 'to_alipay_dict'):
                params['change_body_dto'] = self.change_body_dto.to_alipay_dict()
            else:
                params['change_body_dto'] = self.change_body_dto
        if self.change_scene:
            if hasattr(self.change_scene, 'to_alipay_dict'):
                params['change_scene'] = self.change_scene.to_alipay_dict()
            else:
                params['change_scene'] = self.change_scene
        if self.partner_org_id:
            if hasattr(self.partner_org_id, 'to_alipay_dict'):
                params['partner_org_id'] = self.partner_org_id.to_alipay_dict()
            else:
                params['partner_org_id'] = self.partner_org_id
        if self.pre_order_id:
            if hasattr(self.pre_order_id, 'to_alipay_dict'):
                params['pre_order_id'] = self.pre_order_id.to_alipay_dict()
            else:
                params['pre_order_id'] = self.pre_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneOrderChangeConsultModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'change_body_dto' in d:
            o.change_body_dto = d['change_body_dto']
        if 'change_scene' in d:
            o.change_scene = d['change_scene']
        if 'partner_org_id' in d:
            o.partner_org_id = d['partner_org_id']
        if 'pre_order_id' in d:
            o.pre_order_id = d['pre_order_id']
        return o


