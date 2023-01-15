#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsApplyProductCoverageDTO import InsApplyProductCoverageDTO


class AlipayInsMarketingGiftContractApplyModel(object):

    def __init__(self):
        self._biz_data_for_bx_policy = None
        self._channel = None
        self._contract_no = None
        self._entrance = None
        self._gift_prod_code = None
        self._ins_apply_product_coverage_dto = None
        self._open_id = None
        self._out_biz_no = None
        self._relation_to_apply = None
        self._relation_to_holder = None
        self._right_no = None
        self._source = None
        self._user_id = None

    @property
    def biz_data_for_bx_policy(self):
        return self._biz_data_for_bx_policy

    @biz_data_for_bx_policy.setter
    def biz_data_for_bx_policy(self, value):
        self._biz_data_for_bx_policy = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def contract_no(self):
        return self._contract_no

    @contract_no.setter
    def contract_no(self, value):
        self._contract_no = value
    @property
    def entrance(self):
        return self._entrance

    @entrance.setter
    def entrance(self, value):
        self._entrance = value
    @property
    def gift_prod_code(self):
        return self._gift_prod_code

    @gift_prod_code.setter
    def gift_prod_code(self, value):
        self._gift_prod_code = value
    @property
    def ins_apply_product_coverage_dto(self):
        return self._ins_apply_product_coverage_dto

    @ins_apply_product_coverage_dto.setter
    def ins_apply_product_coverage_dto(self, value):
        if isinstance(value, InsApplyProductCoverageDTO):
            self._ins_apply_product_coverage_dto = value
        else:
            self._ins_apply_product_coverage_dto = InsApplyProductCoverageDTO.from_alipay_dict(value)
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def relation_to_apply(self):
        return self._relation_to_apply

    @relation_to_apply.setter
    def relation_to_apply(self, value):
        self._relation_to_apply = value
    @property
    def relation_to_holder(self):
        return self._relation_to_holder

    @relation_to_holder.setter
    def relation_to_holder(self, value):
        self._relation_to_holder = value
    @property
    def right_no(self):
        return self._right_no

    @right_no.setter
    def right_no(self, value):
        self._right_no = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_data_for_bx_policy:
            if hasattr(self.biz_data_for_bx_policy, 'to_alipay_dict'):
                params['biz_data_for_bx_policy'] = self.biz_data_for_bx_policy.to_alipay_dict()
            else:
                params['biz_data_for_bx_policy'] = self.biz_data_for_bx_policy
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.contract_no:
            if hasattr(self.contract_no, 'to_alipay_dict'):
                params['contract_no'] = self.contract_no.to_alipay_dict()
            else:
                params['contract_no'] = self.contract_no
        if self.entrance:
            if hasattr(self.entrance, 'to_alipay_dict'):
                params['entrance'] = self.entrance.to_alipay_dict()
            else:
                params['entrance'] = self.entrance
        if self.gift_prod_code:
            if hasattr(self.gift_prod_code, 'to_alipay_dict'):
                params['gift_prod_code'] = self.gift_prod_code.to_alipay_dict()
            else:
                params['gift_prod_code'] = self.gift_prod_code
        if self.ins_apply_product_coverage_dto:
            if hasattr(self.ins_apply_product_coverage_dto, 'to_alipay_dict'):
                params['ins_apply_product_coverage_dto'] = self.ins_apply_product_coverage_dto.to_alipay_dict()
            else:
                params['ins_apply_product_coverage_dto'] = self.ins_apply_product_coverage_dto
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.relation_to_apply:
            if hasattr(self.relation_to_apply, 'to_alipay_dict'):
                params['relation_to_apply'] = self.relation_to_apply.to_alipay_dict()
            else:
                params['relation_to_apply'] = self.relation_to_apply
        if self.relation_to_holder:
            if hasattr(self.relation_to_holder, 'to_alipay_dict'):
                params['relation_to_holder'] = self.relation_to_holder.to_alipay_dict()
            else:
                params['relation_to_holder'] = self.relation_to_holder
        if self.right_no:
            if hasattr(self.right_no, 'to_alipay_dict'):
                params['right_no'] = self.right_no.to_alipay_dict()
            else:
                params['right_no'] = self.right_no
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsMarketingGiftContractApplyModel()
        if 'biz_data_for_bx_policy' in d:
            o.biz_data_for_bx_policy = d['biz_data_for_bx_policy']
        if 'channel' in d:
            o.channel = d['channel']
        if 'contract_no' in d:
            o.contract_no = d['contract_no']
        if 'entrance' in d:
            o.entrance = d['entrance']
        if 'gift_prod_code' in d:
            o.gift_prod_code = d['gift_prod_code']
        if 'ins_apply_product_coverage_dto' in d:
            o.ins_apply_product_coverage_dto = d['ins_apply_product_coverage_dto']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'relation_to_apply' in d:
            o.relation_to_apply = d['relation_to_apply']
        if 'relation_to_holder' in d:
            o.relation_to_holder = d['relation_to_holder']
        if 'right_no' in d:
            o.right_no = d['right_no']
        if 'source' in d:
            o.source = d['source']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


