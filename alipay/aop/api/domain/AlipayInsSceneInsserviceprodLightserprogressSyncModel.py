#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneInsserviceprodLightserprogressSyncModel(object):

    def __init__(self):
        self._biz_data = None
        self._inst_action_url = None
        self._inst_apply_order_no = None
        self._inst_node_code = None
        self._inst_policy_no = None
        self._inst_prod_item_no = None
        self._inst_progress_no = None
        self._order_create_time = None
        self._progress_create_time = None

    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        self._biz_data = value
    @property
    def inst_action_url(self):
        return self._inst_action_url

    @inst_action_url.setter
    def inst_action_url(self, value):
        self._inst_action_url = value
    @property
    def inst_apply_order_no(self):
        return self._inst_apply_order_no

    @inst_apply_order_no.setter
    def inst_apply_order_no(self, value):
        self._inst_apply_order_no = value
    @property
    def inst_node_code(self):
        return self._inst_node_code

    @inst_node_code.setter
    def inst_node_code(self, value):
        self._inst_node_code = value
    @property
    def inst_policy_no(self):
        return self._inst_policy_no

    @inst_policy_no.setter
    def inst_policy_no(self, value):
        self._inst_policy_no = value
    @property
    def inst_prod_item_no(self):
        return self._inst_prod_item_no

    @inst_prod_item_no.setter
    def inst_prod_item_no(self, value):
        self._inst_prod_item_no = value
    @property
    def inst_progress_no(self):
        return self._inst_progress_no

    @inst_progress_no.setter
    def inst_progress_no(self, value):
        self._inst_progress_no = value
    @property
    def order_create_time(self):
        return self._order_create_time

    @order_create_time.setter
    def order_create_time(self, value):
        self._order_create_time = value
    @property
    def progress_create_time(self):
        return self._progress_create_time

    @progress_create_time.setter
    def progress_create_time(self, value):
        self._progress_create_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_data:
            if hasattr(self.biz_data, 'to_alipay_dict'):
                params['biz_data'] = self.biz_data.to_alipay_dict()
            else:
                params['biz_data'] = self.biz_data
        if self.inst_action_url:
            if hasattr(self.inst_action_url, 'to_alipay_dict'):
                params['inst_action_url'] = self.inst_action_url.to_alipay_dict()
            else:
                params['inst_action_url'] = self.inst_action_url
        if self.inst_apply_order_no:
            if hasattr(self.inst_apply_order_no, 'to_alipay_dict'):
                params['inst_apply_order_no'] = self.inst_apply_order_no.to_alipay_dict()
            else:
                params['inst_apply_order_no'] = self.inst_apply_order_no
        if self.inst_node_code:
            if hasattr(self.inst_node_code, 'to_alipay_dict'):
                params['inst_node_code'] = self.inst_node_code.to_alipay_dict()
            else:
                params['inst_node_code'] = self.inst_node_code
        if self.inst_policy_no:
            if hasattr(self.inst_policy_no, 'to_alipay_dict'):
                params['inst_policy_no'] = self.inst_policy_no.to_alipay_dict()
            else:
                params['inst_policy_no'] = self.inst_policy_no
        if self.inst_prod_item_no:
            if hasattr(self.inst_prod_item_no, 'to_alipay_dict'):
                params['inst_prod_item_no'] = self.inst_prod_item_no.to_alipay_dict()
            else:
                params['inst_prod_item_no'] = self.inst_prod_item_no
        if self.inst_progress_no:
            if hasattr(self.inst_progress_no, 'to_alipay_dict'):
                params['inst_progress_no'] = self.inst_progress_no.to_alipay_dict()
            else:
                params['inst_progress_no'] = self.inst_progress_no
        if self.order_create_time:
            if hasattr(self.order_create_time, 'to_alipay_dict'):
                params['order_create_time'] = self.order_create_time.to_alipay_dict()
            else:
                params['order_create_time'] = self.order_create_time
        if self.progress_create_time:
            if hasattr(self.progress_create_time, 'to_alipay_dict'):
                params['progress_create_time'] = self.progress_create_time.to_alipay_dict()
            else:
                params['progress_create_time'] = self.progress_create_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneInsserviceprodLightserprogressSyncModel()
        if 'biz_data' in d:
            o.biz_data = d['biz_data']
        if 'inst_action_url' in d:
            o.inst_action_url = d['inst_action_url']
        if 'inst_apply_order_no' in d:
            o.inst_apply_order_no = d['inst_apply_order_no']
        if 'inst_node_code' in d:
            o.inst_node_code = d['inst_node_code']
        if 'inst_policy_no' in d:
            o.inst_policy_no = d['inst_policy_no']
        if 'inst_prod_item_no' in d:
            o.inst_prod_item_no = d['inst_prod_item_no']
        if 'inst_progress_no' in d:
            o.inst_progress_no = d['inst_progress_no']
        if 'order_create_time' in d:
            o.order_create_time = d['order_create_time']
        if 'progress_create_time' in d:
            o.progress_create_time = d['progress_create_time']
        return o


