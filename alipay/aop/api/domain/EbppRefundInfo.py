#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EbppRefundInfo(object):

    def __init__(self):
        self._biz_type = None
        self._charge_inst = None
        self._chargeoff_inst = None
        self._gmt_create = None
        self._gmt_refund = None
        self._out_ext_id = None
        self._refund_amount = None
        self._refund_id = None
        self._refund_payment_id = None
        self._refund_reason = None
        self._refund_status = None
        self._refund_type = None
        self._retry_times = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def charge_inst(self):
        return self._charge_inst

    @charge_inst.setter
    def charge_inst(self, value):
        self._charge_inst = value
    @property
    def chargeoff_inst(self):
        return self._chargeoff_inst

    @chargeoff_inst.setter
    def chargeoff_inst(self, value):
        self._chargeoff_inst = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_refund(self):
        return self._gmt_refund

    @gmt_refund.setter
    def gmt_refund(self, value):
        self._gmt_refund = value
    @property
    def out_ext_id(self):
        return self._out_ext_id

    @out_ext_id.setter
    def out_ext_id(self, value):
        self._out_ext_id = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_id(self):
        return self._refund_id

    @refund_id.setter
    def refund_id(self, value):
        self._refund_id = value
    @property
    def refund_payment_id(self):
        return self._refund_payment_id

    @refund_payment_id.setter
    def refund_payment_id(self, value):
        self._refund_payment_id = value
    @property
    def refund_reason(self):
        return self._refund_reason

    @refund_reason.setter
    def refund_reason(self, value):
        self._refund_reason = value
    @property
    def refund_status(self):
        return self._refund_status

    @refund_status.setter
    def refund_status(self, value):
        self._refund_status = value
    @property
    def refund_type(self):
        return self._refund_type

    @refund_type.setter
    def refund_type(self, value):
        self._refund_type = value
    @property
    def retry_times(self):
        return self._retry_times

    @retry_times.setter
    def retry_times(self, value):
        self._retry_times = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.charge_inst:
            if hasattr(self.charge_inst, 'to_alipay_dict'):
                params['charge_inst'] = self.charge_inst.to_alipay_dict()
            else:
                params['charge_inst'] = self.charge_inst
        if self.chargeoff_inst:
            if hasattr(self.chargeoff_inst, 'to_alipay_dict'):
                params['chargeoff_inst'] = self.chargeoff_inst.to_alipay_dict()
            else:
                params['chargeoff_inst'] = self.chargeoff_inst
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_refund:
            if hasattr(self.gmt_refund, 'to_alipay_dict'):
                params['gmt_refund'] = self.gmt_refund.to_alipay_dict()
            else:
                params['gmt_refund'] = self.gmt_refund
        if self.out_ext_id:
            if hasattr(self.out_ext_id, 'to_alipay_dict'):
                params['out_ext_id'] = self.out_ext_id.to_alipay_dict()
            else:
                params['out_ext_id'] = self.out_ext_id
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_id:
            if hasattr(self.refund_id, 'to_alipay_dict'):
                params['refund_id'] = self.refund_id.to_alipay_dict()
            else:
                params['refund_id'] = self.refund_id
        if self.refund_payment_id:
            if hasattr(self.refund_payment_id, 'to_alipay_dict'):
                params['refund_payment_id'] = self.refund_payment_id.to_alipay_dict()
            else:
                params['refund_payment_id'] = self.refund_payment_id
        if self.refund_reason:
            if hasattr(self.refund_reason, 'to_alipay_dict'):
                params['refund_reason'] = self.refund_reason.to_alipay_dict()
            else:
                params['refund_reason'] = self.refund_reason
        if self.refund_status:
            if hasattr(self.refund_status, 'to_alipay_dict'):
                params['refund_status'] = self.refund_status.to_alipay_dict()
            else:
                params['refund_status'] = self.refund_status
        if self.refund_type:
            if hasattr(self.refund_type, 'to_alipay_dict'):
                params['refund_type'] = self.refund_type.to_alipay_dict()
            else:
                params['refund_type'] = self.refund_type
        if self.retry_times:
            if hasattr(self.retry_times, 'to_alipay_dict'):
                params['retry_times'] = self.retry_times.to_alipay_dict()
            else:
                params['retry_times'] = self.retry_times
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EbppRefundInfo()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'charge_inst' in d:
            o.charge_inst = d['charge_inst']
        if 'chargeoff_inst' in d:
            o.chargeoff_inst = d['chargeoff_inst']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_refund' in d:
            o.gmt_refund = d['gmt_refund']
        if 'out_ext_id' in d:
            o.out_ext_id = d['out_ext_id']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_id' in d:
            o.refund_id = d['refund_id']
        if 'refund_payment_id' in d:
            o.refund_payment_id = d['refund_payment_id']
        if 'refund_reason' in d:
            o.refund_reason = d['refund_reason']
        if 'refund_status' in d:
            o.refund_status = d['refund_status']
        if 'refund_type' in d:
            o.refund_type = d['refund_type']
        if 'retry_times' in d:
            o.retry_times = d['retry_times']
        return o


