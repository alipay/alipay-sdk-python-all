#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsOpenPreOrderBizData import InsOpenPreOrderBizData
from alipay.aop.api.domain.InsOpenUserDTO import InsOpenUserDTO
from alipay.aop.api.domain.InsOpenUserDTO import InsOpenUserDTO


class AlipayInsSceneCommonPreOrderModel(object):

    def __init__(self):
        self._auto_renewal = None
        self._biz_data = None
        self._holder_user = None
        self._insured_user = None
        self._out_biz_no = None
        self._partner_org_id = None
        self._quote_id = None
        self._recommend_flow_id = None
        self._user_client = None

    @property
    def auto_renewal(self):
        return self._auto_renewal

    @auto_renewal.setter
    def auto_renewal(self, value):
        self._auto_renewal = value
    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        if isinstance(value, InsOpenPreOrderBizData):
            self._biz_data = value
        else:
            self._biz_data = InsOpenPreOrderBizData.from_alipay_dict(value)
    @property
    def holder_user(self):
        return self._holder_user

    @holder_user.setter
    def holder_user(self, value):
        if isinstance(value, InsOpenUserDTO):
            self._holder_user = value
        else:
            self._holder_user = InsOpenUserDTO.from_alipay_dict(value)
    @property
    def insured_user(self):
        return self._insured_user

    @insured_user.setter
    def insured_user(self, value):
        if isinstance(value, InsOpenUserDTO):
            self._insured_user = value
        else:
            self._insured_user = InsOpenUserDTO.from_alipay_dict(value)
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def partner_org_id(self):
        return self._partner_org_id

    @partner_org_id.setter
    def partner_org_id(self, value):
        self._partner_org_id = value
    @property
    def quote_id(self):
        return self._quote_id

    @quote_id.setter
    def quote_id(self, value):
        self._quote_id = value
    @property
    def recommend_flow_id(self):
        return self._recommend_flow_id

    @recommend_flow_id.setter
    def recommend_flow_id(self, value):
        self._recommend_flow_id = value
    @property
    def user_client(self):
        return self._user_client

    @user_client.setter
    def user_client(self, value):
        self._user_client = value


    def to_alipay_dict(self):
        params = dict()
        if self.auto_renewal:
            if hasattr(self.auto_renewal, 'to_alipay_dict'):
                params['auto_renewal'] = self.auto_renewal.to_alipay_dict()
            else:
                params['auto_renewal'] = self.auto_renewal
        if self.biz_data:
            if hasattr(self.biz_data, 'to_alipay_dict'):
                params['biz_data'] = self.biz_data.to_alipay_dict()
            else:
                params['biz_data'] = self.biz_data
        if self.holder_user:
            if hasattr(self.holder_user, 'to_alipay_dict'):
                params['holder_user'] = self.holder_user.to_alipay_dict()
            else:
                params['holder_user'] = self.holder_user
        if self.insured_user:
            if hasattr(self.insured_user, 'to_alipay_dict'):
                params['insured_user'] = self.insured_user.to_alipay_dict()
            else:
                params['insured_user'] = self.insured_user
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.partner_org_id:
            if hasattr(self.partner_org_id, 'to_alipay_dict'):
                params['partner_org_id'] = self.partner_org_id.to_alipay_dict()
            else:
                params['partner_org_id'] = self.partner_org_id
        if self.quote_id:
            if hasattr(self.quote_id, 'to_alipay_dict'):
                params['quote_id'] = self.quote_id.to_alipay_dict()
            else:
                params['quote_id'] = self.quote_id
        if self.recommend_flow_id:
            if hasattr(self.recommend_flow_id, 'to_alipay_dict'):
                params['recommend_flow_id'] = self.recommend_flow_id.to_alipay_dict()
            else:
                params['recommend_flow_id'] = self.recommend_flow_id
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
        o = AlipayInsSceneCommonPreOrderModel()
        if 'auto_renewal' in d:
            o.auto_renewal = d['auto_renewal']
        if 'biz_data' in d:
            o.biz_data = d['biz_data']
        if 'holder_user' in d:
            o.holder_user = d['holder_user']
        if 'insured_user' in d:
            o.insured_user = d['insured_user']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'partner_org_id' in d:
            o.partner_org_id = d['partner_org_id']
        if 'quote_id' in d:
            o.quote_id = d['quote_id']
        if 'recommend_flow_id' in d:
            o.recommend_flow_id = d['recommend_flow_id']
        if 'user_client' in d:
            o.user_client = d['user_client']
        return o


