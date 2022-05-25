#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInstserviceTokenCreateModel(object):

    def __init__(self):
        self._agent_channel = None
        self._agent_code = None
        self._bill_key = None
        self._biz_scene = None
        self._biz_type = None
        self._deduct_amount = None
        self._ededuct_product_code = None
        self._execute_date = None
        self._inst_id = None
        self._out_agreement_id = None
        self._pay_mode = None
        self._service_desc = None
        self._sub_biz_type = None
        self._threshold_amount = None
        self._title = None

    @property
    def agent_channel(self):
        return self._agent_channel

    @agent_channel.setter
    def agent_channel(self, value):
        self._agent_channel = value
    @property
    def agent_code(self):
        return self._agent_code

    @agent_code.setter
    def agent_code(self, value):
        self._agent_code = value
    @property
    def bill_key(self):
        return self._bill_key

    @bill_key.setter
    def bill_key(self, value):
        self._bill_key = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def deduct_amount(self):
        return self._deduct_amount

    @deduct_amount.setter
    def deduct_amount(self, value):
        self._deduct_amount = value
    @property
    def ededuct_product_code(self):
        return self._ededuct_product_code

    @ededuct_product_code.setter
    def ededuct_product_code(self, value):
        self._ededuct_product_code = value
    @property
    def execute_date(self):
        return self._execute_date

    @execute_date.setter
    def execute_date(self, value):
        self._execute_date = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def out_agreement_id(self):
        return self._out_agreement_id

    @out_agreement_id.setter
    def out_agreement_id(self, value):
        self._out_agreement_id = value
    @property
    def pay_mode(self):
        return self._pay_mode

    @pay_mode.setter
    def pay_mode(self, value):
        self._pay_mode = value
    @property
    def service_desc(self):
        return self._service_desc

    @service_desc.setter
    def service_desc(self, value):
        self._service_desc = value
    @property
    def sub_biz_type(self):
        return self._sub_biz_type

    @sub_biz_type.setter
    def sub_biz_type(self, value):
        self._sub_biz_type = value
    @property
    def threshold_amount(self):
        return self._threshold_amount

    @threshold_amount.setter
    def threshold_amount(self, value):
        self._threshold_amount = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_channel:
            if hasattr(self.agent_channel, 'to_alipay_dict'):
                params['agent_channel'] = self.agent_channel.to_alipay_dict()
            else:
                params['agent_channel'] = self.agent_channel
        if self.agent_code:
            if hasattr(self.agent_code, 'to_alipay_dict'):
                params['agent_code'] = self.agent_code.to_alipay_dict()
            else:
                params['agent_code'] = self.agent_code
        if self.bill_key:
            if hasattr(self.bill_key, 'to_alipay_dict'):
                params['bill_key'] = self.bill_key.to_alipay_dict()
            else:
                params['bill_key'] = self.bill_key
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.deduct_amount:
            if hasattr(self.deduct_amount, 'to_alipay_dict'):
                params['deduct_amount'] = self.deduct_amount.to_alipay_dict()
            else:
                params['deduct_amount'] = self.deduct_amount
        if self.ededuct_product_code:
            if hasattr(self.ededuct_product_code, 'to_alipay_dict'):
                params['ededuct_product_code'] = self.ededuct_product_code.to_alipay_dict()
            else:
                params['ededuct_product_code'] = self.ededuct_product_code
        if self.execute_date:
            if hasattr(self.execute_date, 'to_alipay_dict'):
                params['execute_date'] = self.execute_date.to_alipay_dict()
            else:
                params['execute_date'] = self.execute_date
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.out_agreement_id:
            if hasattr(self.out_agreement_id, 'to_alipay_dict'):
                params['out_agreement_id'] = self.out_agreement_id.to_alipay_dict()
            else:
                params['out_agreement_id'] = self.out_agreement_id
        if self.pay_mode:
            if hasattr(self.pay_mode, 'to_alipay_dict'):
                params['pay_mode'] = self.pay_mode.to_alipay_dict()
            else:
                params['pay_mode'] = self.pay_mode
        if self.service_desc:
            if hasattr(self.service_desc, 'to_alipay_dict'):
                params['service_desc'] = self.service_desc.to_alipay_dict()
            else:
                params['service_desc'] = self.service_desc
        if self.sub_biz_type:
            if hasattr(self.sub_biz_type, 'to_alipay_dict'):
                params['sub_biz_type'] = self.sub_biz_type.to_alipay_dict()
            else:
                params['sub_biz_type'] = self.sub_biz_type
        if self.threshold_amount:
            if hasattr(self.threshold_amount, 'to_alipay_dict'):
                params['threshold_amount'] = self.threshold_amount.to_alipay_dict()
            else:
                params['threshold_amount'] = self.threshold_amount
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInstserviceTokenCreateModel()
        if 'agent_channel' in d:
            o.agent_channel = d['agent_channel']
        if 'agent_code' in d:
            o.agent_code = d['agent_code']
        if 'bill_key' in d:
            o.bill_key = d['bill_key']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'deduct_amount' in d:
            o.deduct_amount = d['deduct_amount']
        if 'ededuct_product_code' in d:
            o.ededuct_product_code = d['ededuct_product_code']
        if 'execute_date' in d:
            o.execute_date = d['execute_date']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'out_agreement_id' in d:
            o.out_agreement_id = d['out_agreement_id']
        if 'pay_mode' in d:
            o.pay_mode = d['pay_mode']
        if 'service_desc' in d:
            o.service_desc = d['service_desc']
        if 'sub_biz_type' in d:
            o.sub_biz_type = d['sub_biz_type']
        if 'threshold_amount' in d:
            o.threshold_amount = d['threshold_amount']
        if 'title' in d:
            o.title = d['title']
        return o


