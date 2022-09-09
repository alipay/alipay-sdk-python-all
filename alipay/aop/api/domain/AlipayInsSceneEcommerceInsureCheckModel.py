#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsureAdmitDTO import InsureAdmitDTO


class AlipayInsSceneEcommerceInsureCheckModel(object):

    def __init__(self):
        self._insure_admit_dto_list = None
        self._partner_org_id = None
        self._product_code = None
        self._scene_code = None
        self._user_client = None

    @property
    def insure_admit_dto_list(self):
        return self._insure_admit_dto_list

    @insure_admit_dto_list.setter
    def insure_admit_dto_list(self, value):
        if isinstance(value, list):
            self._insure_admit_dto_list = list()
            for i in value:
                if isinstance(i, InsureAdmitDTO):
                    self._insure_admit_dto_list.append(i)
                else:
                    self._insure_admit_dto_list.append(InsureAdmitDTO.from_alipay_dict(i))
    @property
    def partner_org_id(self):
        return self._partner_org_id

    @partner_org_id.setter
    def partner_org_id(self, value):
        self._partner_org_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def user_client(self):
        return self._user_client

    @user_client.setter
    def user_client(self, value):
        self._user_client = value


    def to_alipay_dict(self):
        params = dict()
        if self.insure_admit_dto_list:
            if isinstance(self.insure_admit_dto_list, list):
                for i in range(0, len(self.insure_admit_dto_list)):
                    element = self.insure_admit_dto_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.insure_admit_dto_list[i] = element.to_alipay_dict()
            if hasattr(self.insure_admit_dto_list, 'to_alipay_dict'):
                params['insure_admit_dto_list'] = self.insure_admit_dto_list.to_alipay_dict()
            else:
                params['insure_admit_dto_list'] = self.insure_admit_dto_list
        if self.partner_org_id:
            if hasattr(self.partner_org_id, 'to_alipay_dict'):
                params['partner_org_id'] = self.partner_org_id.to_alipay_dict()
            else:
                params['partner_org_id'] = self.partner_org_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.user_client:
            if hasattr(self.user_client, 'to_alipay_dict'):
                params['user_client'] = self.user_client.to_alipay_dict()
            else:
                params['user_client'] = self.user_client
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneEcommerceInsureCheckModel()
        if 'insure_admit_dto_list' in d:
            o.insure_admit_dto_list = d['insure_admit_dto_list']
        if 'partner_org_id' in d:
            o.partner_org_id = d['partner_org_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'user_client' in d:
            o.user_client = d['user_client']
        return o


