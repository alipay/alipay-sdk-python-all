#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Participant import Participant
from alipay.aop.api.domain.TransOrderDetail import TransOrderDetail


class AlipayFundBatchUniTransferModel(object):

    def __init__(self):
        self._biz_scene = None
        self._business_params = None
        self._original_order_id = None
        self._out_batch_no = None
        self._payer_info = None
        self._product_code = None
        self._remark = None
        self._total_count = None
        self._total_trans_amount = None
        self._trans_order_list = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def business_params(self):
        return self._business_params

    @business_params.setter
    def business_params(self, value):
        self._business_params = value
    @property
    def original_order_id(self):
        return self._original_order_id

    @original_order_id.setter
    def original_order_id(self, value):
        self._original_order_id = value
    @property
    def out_batch_no(self):
        return self._out_batch_no

    @out_batch_no.setter
    def out_batch_no(self, value):
        self._out_batch_no = value
    @property
    def payer_info(self):
        return self._payer_info

    @payer_info.setter
    def payer_info(self, value):
        if isinstance(value, Participant):
            self._payer_info = value
        else:
            self._payer_info = Participant.from_alipay_dict(value)
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value
    @property
    def total_trans_amount(self):
        return self._total_trans_amount

    @total_trans_amount.setter
    def total_trans_amount(self, value):
        self._total_trans_amount = value
    @property
    def trans_order_list(self):
        return self._trans_order_list

    @trans_order_list.setter
    def trans_order_list(self, value):
        if isinstance(value, list):
            self._trans_order_list = list()
            for i in value:
                if isinstance(i, TransOrderDetail):
                    self._trans_order_list.append(i)
                else:
                    self._trans_order_list.append(TransOrderDetail.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.business_params:
            if hasattr(self.business_params, 'to_alipay_dict'):
                params['business_params'] = self.business_params.to_alipay_dict()
            else:
                params['business_params'] = self.business_params
        if self.original_order_id:
            if hasattr(self.original_order_id, 'to_alipay_dict'):
                params['original_order_id'] = self.original_order_id.to_alipay_dict()
            else:
                params['original_order_id'] = self.original_order_id
        if self.out_batch_no:
            if hasattr(self.out_batch_no, 'to_alipay_dict'):
                params['out_batch_no'] = self.out_batch_no.to_alipay_dict()
            else:
                params['out_batch_no'] = self.out_batch_no
        if self.payer_info:
            if hasattr(self.payer_info, 'to_alipay_dict'):
                params['payer_info'] = self.payer_info.to_alipay_dict()
            else:
                params['payer_info'] = self.payer_info
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.total_count:
            if hasattr(self.total_count, 'to_alipay_dict'):
                params['total_count'] = self.total_count.to_alipay_dict()
            else:
                params['total_count'] = self.total_count
        if self.total_trans_amount:
            if hasattr(self.total_trans_amount, 'to_alipay_dict'):
                params['total_trans_amount'] = self.total_trans_amount.to_alipay_dict()
            else:
                params['total_trans_amount'] = self.total_trans_amount
        if self.trans_order_list:
            if isinstance(self.trans_order_list, list):
                for i in range(0, len(self.trans_order_list)):
                    element = self.trans_order_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.trans_order_list[i] = element.to_alipay_dict()
            if hasattr(self.trans_order_list, 'to_alipay_dict'):
                params['trans_order_list'] = self.trans_order_list.to_alipay_dict()
            else:
                params['trans_order_list'] = self.trans_order_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundBatchUniTransferModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'business_params' in d:
            o.business_params = d['business_params']
        if 'original_order_id' in d:
            o.original_order_id = d['original_order_id']
        if 'out_batch_no' in d:
            o.out_batch_no = d['out_batch_no']
        if 'payer_info' in d:
            o.payer_info = d['payer_info']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'remark' in d:
            o.remark = d['remark']
        if 'total_count' in d:
            o.total_count = d['total_count']
        if 'total_trans_amount' in d:
            o.total_trans_amount = d['total_trans_amount']
        if 'trans_order_list' in d:
            o.trans_order_list = d['trans_order_list']
        return o


