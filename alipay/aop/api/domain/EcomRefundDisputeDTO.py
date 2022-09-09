#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EcomRefundDisputeDTO(object):

    def __init__(self):
        self._buyer_id = None
        self._buyer_logistic_company_code = None
        self._buyer_logistic_company_name = None
        self._buyer_logistic_no = None
        self._case_time = None
        self._end_time = None
        self._goods_needs = None
        self._goods_status = None
        self._order_id = None
        self._reason_code = None
        self._reason_text = None
        self._refund_desc = None
        self._refund_dispute_id = None
        self._refund_fee = None
        self._refund_status = None
        self._refund_type = None
        self._seller_id = None
        self._start_time = None

    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def buyer_logistic_company_code(self):
        return self._buyer_logistic_company_code

    @buyer_logistic_company_code.setter
    def buyer_logistic_company_code(self, value):
        self._buyer_logistic_company_code = value
    @property
    def buyer_logistic_company_name(self):
        return self._buyer_logistic_company_name

    @buyer_logistic_company_name.setter
    def buyer_logistic_company_name(self, value):
        self._buyer_logistic_company_name = value
    @property
    def buyer_logistic_no(self):
        return self._buyer_logistic_no

    @buyer_logistic_no.setter
    def buyer_logistic_no(self, value):
        self._buyer_logistic_no = value
    @property
    def case_time(self):
        return self._case_time

    @case_time.setter
    def case_time(self, value):
        self._case_time = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def goods_needs(self):
        return self._goods_needs

    @goods_needs.setter
    def goods_needs(self, value):
        self._goods_needs = value
    @property
    def goods_status(self):
        return self._goods_status

    @goods_status.setter
    def goods_status(self, value):
        self._goods_status = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def reason_code(self):
        return self._reason_code

    @reason_code.setter
    def reason_code(self, value):
        self._reason_code = value
    @property
    def reason_text(self):
        return self._reason_text

    @reason_text.setter
    def reason_text(self, value):
        self._reason_text = value
    @property
    def refund_desc(self):
        return self._refund_desc

    @refund_desc.setter
    def refund_desc(self, value):
        self._refund_desc = value
    @property
    def refund_dispute_id(self):
        return self._refund_dispute_id

    @refund_dispute_id.setter
    def refund_dispute_id(self, value):
        self._refund_dispute_id = value
    @property
    def refund_fee(self):
        return self._refund_fee

    @refund_fee.setter
    def refund_fee(self, value):
        self._refund_fee = value
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
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.buyer_logistic_company_code:
            if hasattr(self.buyer_logistic_company_code, 'to_alipay_dict'):
                params['buyer_logistic_company_code'] = self.buyer_logistic_company_code.to_alipay_dict()
            else:
                params['buyer_logistic_company_code'] = self.buyer_logistic_company_code
        if self.buyer_logistic_company_name:
            if hasattr(self.buyer_logistic_company_name, 'to_alipay_dict'):
                params['buyer_logistic_company_name'] = self.buyer_logistic_company_name.to_alipay_dict()
            else:
                params['buyer_logistic_company_name'] = self.buyer_logistic_company_name
        if self.buyer_logistic_no:
            if hasattr(self.buyer_logistic_no, 'to_alipay_dict'):
                params['buyer_logistic_no'] = self.buyer_logistic_no.to_alipay_dict()
            else:
                params['buyer_logistic_no'] = self.buyer_logistic_no
        if self.case_time:
            if hasattr(self.case_time, 'to_alipay_dict'):
                params['case_time'] = self.case_time.to_alipay_dict()
            else:
                params['case_time'] = self.case_time
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.goods_needs:
            if hasattr(self.goods_needs, 'to_alipay_dict'):
                params['goods_needs'] = self.goods_needs.to_alipay_dict()
            else:
                params['goods_needs'] = self.goods_needs
        if self.goods_status:
            if hasattr(self.goods_status, 'to_alipay_dict'):
                params['goods_status'] = self.goods_status.to_alipay_dict()
            else:
                params['goods_status'] = self.goods_status
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.reason_code:
            if hasattr(self.reason_code, 'to_alipay_dict'):
                params['reason_code'] = self.reason_code.to_alipay_dict()
            else:
                params['reason_code'] = self.reason_code
        if self.reason_text:
            if hasattr(self.reason_text, 'to_alipay_dict'):
                params['reason_text'] = self.reason_text.to_alipay_dict()
            else:
                params['reason_text'] = self.reason_text
        if self.refund_desc:
            if hasattr(self.refund_desc, 'to_alipay_dict'):
                params['refund_desc'] = self.refund_desc.to_alipay_dict()
            else:
                params['refund_desc'] = self.refund_desc
        if self.refund_dispute_id:
            if hasattr(self.refund_dispute_id, 'to_alipay_dict'):
                params['refund_dispute_id'] = self.refund_dispute_id.to_alipay_dict()
            else:
                params['refund_dispute_id'] = self.refund_dispute_id
        if self.refund_fee:
            if hasattr(self.refund_fee, 'to_alipay_dict'):
                params['refund_fee'] = self.refund_fee.to_alipay_dict()
            else:
                params['refund_fee'] = self.refund_fee
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
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EcomRefundDisputeDTO()
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'buyer_logistic_company_code' in d:
            o.buyer_logistic_company_code = d['buyer_logistic_company_code']
        if 'buyer_logistic_company_name' in d:
            o.buyer_logistic_company_name = d['buyer_logistic_company_name']
        if 'buyer_logistic_no' in d:
            o.buyer_logistic_no = d['buyer_logistic_no']
        if 'case_time' in d:
            o.case_time = d['case_time']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'goods_needs' in d:
            o.goods_needs = d['goods_needs']
        if 'goods_status' in d:
            o.goods_status = d['goods_status']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'reason_code' in d:
            o.reason_code = d['reason_code']
        if 'reason_text' in d:
            o.reason_text = d['reason_text']
        if 'refund_desc' in d:
            o.refund_desc = d['refund_desc']
        if 'refund_dispute_id' in d:
            o.refund_dispute_id = d['refund_dispute_id']
        if 'refund_fee' in d:
            o.refund_fee = d['refund_fee']
        if 'refund_status' in d:
            o.refund_status = d['refund_status']
        if 'refund_type' in d:
            o.refund_type = d['refund_type']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


