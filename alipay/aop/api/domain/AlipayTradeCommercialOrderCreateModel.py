#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeCommercialOrderCreateModel(object):

    def __init__(self):
        self._agent_type = None
        self._customer_id = None
        self._extend_params = None
        self._initiator_type = None
        self._metadata = None
        self._order_amount = None
        self._page_code = None
        self._price_id = None
        self._redirect_url = None
        self._ui_mode = None

    @property
    def agent_type(self):
        return self._agent_type

    @agent_type.setter
    def agent_type(self, value):
        self._agent_type = value
    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        self._extend_params = value
    @property
    def initiator_type(self):
        return self._initiator_type

    @initiator_type.setter
    def initiator_type(self, value):
        self._initiator_type = value
    @property
    def metadata(self):
        return self._metadata

    @metadata.setter
    def metadata(self, value):
        self._metadata = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def page_code(self):
        return self._page_code

    @page_code.setter
    def page_code(self, value):
        self._page_code = value
    @property
    def price_id(self):
        return self._price_id

    @price_id.setter
    def price_id(self, value):
        self._price_id = value
    @property
    def redirect_url(self):
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, value):
        self._redirect_url = value
    @property
    def ui_mode(self):
        return self._ui_mode

    @ui_mode.setter
    def ui_mode(self, value):
        self._ui_mode = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_type:
            if hasattr(self.agent_type, 'to_alipay_dict'):
                params['agent_type'] = self.agent_type.to_alipay_dict()
            else:
                params['agent_type'] = self.agent_type
        if self.customer_id:
            if hasattr(self.customer_id, 'to_alipay_dict'):
                params['customer_id'] = self.customer_id.to_alipay_dict()
            else:
                params['customer_id'] = self.customer_id
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.initiator_type:
            if hasattr(self.initiator_type, 'to_alipay_dict'):
                params['initiator_type'] = self.initiator_type.to_alipay_dict()
            else:
                params['initiator_type'] = self.initiator_type
        if self.metadata:
            if hasattr(self.metadata, 'to_alipay_dict'):
                params['metadata'] = self.metadata.to_alipay_dict()
            else:
                params['metadata'] = self.metadata
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.page_code:
            if hasattr(self.page_code, 'to_alipay_dict'):
                params['page_code'] = self.page_code.to_alipay_dict()
            else:
                params['page_code'] = self.page_code
        if self.price_id:
            if hasattr(self.price_id, 'to_alipay_dict'):
                params['price_id'] = self.price_id.to_alipay_dict()
            else:
                params['price_id'] = self.price_id
        if self.redirect_url:
            if hasattr(self.redirect_url, 'to_alipay_dict'):
                params['redirect_url'] = self.redirect_url.to_alipay_dict()
            else:
                params['redirect_url'] = self.redirect_url
        if self.ui_mode:
            if hasattr(self.ui_mode, 'to_alipay_dict'):
                params['ui_mode'] = self.ui_mode.to_alipay_dict()
            else:
                params['ui_mode'] = self.ui_mode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeCommercialOrderCreateModel()
        if 'agent_type' in d:
            o.agent_type = d['agent_type']
        if 'customer_id' in d:
            o.customer_id = d['customer_id']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'initiator_type' in d:
            o.initiator_type = d['initiator_type']
        if 'metadata' in d:
            o.metadata = d['metadata']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'page_code' in d:
            o.page_code = d['page_code']
        if 'price_id' in d:
            o.price_id = d['price_id']
        if 'redirect_url' in d:
            o.redirect_url = d['redirect_url']
        if 'ui_mode' in d:
            o.ui_mode = d['ui_mode']
        return o


