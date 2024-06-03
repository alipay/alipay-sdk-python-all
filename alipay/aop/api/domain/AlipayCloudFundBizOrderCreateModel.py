#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudFundBizOrderCreateModel(object):

    def __init__(self):
        self._amount = None
        self._biz_industry = None
        self._buyer_id = None
        self._buyer_open_id = None
        self._ext_params = None
        self._item_detail = None
        self._logistic_status = None
        self._order_created_time = None
        self._order_id = None
        self._order_status = None
        self._out_order_no = None
        self._pay_order_id = None
        self._pay_status = None
        self._real_amount = None
        self._seller_id = None
        self._seller_open_id = None
        self._service_type = None
        self._source = None
        self._subject = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def biz_industry(self):
        return self._biz_industry

    @biz_industry.setter
    def biz_industry(self, value):
        self._biz_industry = value
    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def buyer_open_id(self):
        return self._buyer_open_id

    @buyer_open_id.setter
    def buyer_open_id(self, value):
        self._buyer_open_id = value
    @property
    def ext_params(self):
        return self._ext_params

    @ext_params.setter
    def ext_params(self, value):
        self._ext_params = value
    @property
    def item_detail(self):
        return self._item_detail

    @item_detail.setter
    def item_detail(self, value):
        if isinstance(value, list):
            self._item_detail = list()
            for i in value:
                self._item_detail.append(i)
    @property
    def logistic_status(self):
        return self._logistic_status

    @logistic_status.setter
    def logistic_status(self, value):
        self._logistic_status = value
    @property
    def order_created_time(self):
        return self._order_created_time

    @order_created_time.setter
    def order_created_time(self, value):
        self._order_created_time = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def pay_order_id(self):
        return self._pay_order_id

    @pay_order_id.setter
    def pay_order_id(self, value):
        self._pay_order_id = value
    @property
    def pay_status(self):
        return self._pay_status

    @pay_status.setter
    def pay_status(self, value):
        self._pay_status = value
    @property
    def real_amount(self):
        return self._real_amount

    @real_amount.setter
    def real_amount(self, value):
        self._real_amount = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def seller_open_id(self):
        return self._seller_open_id

    @seller_open_id.setter
    def seller_open_id(self, value):
        self._seller_open_id = value
    @property
    def service_type(self):
        return self._service_type

    @service_type.setter
    def service_type(self, value):
        self._service_type = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.biz_industry:
            if hasattr(self.biz_industry, 'to_alipay_dict'):
                params['biz_industry'] = self.biz_industry.to_alipay_dict()
            else:
                params['biz_industry'] = self.biz_industry
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.buyer_open_id:
            if hasattr(self.buyer_open_id, 'to_alipay_dict'):
                params['buyer_open_id'] = self.buyer_open_id.to_alipay_dict()
            else:
                params['buyer_open_id'] = self.buyer_open_id
        if self.ext_params:
            if hasattr(self.ext_params, 'to_alipay_dict'):
                params['ext_params'] = self.ext_params.to_alipay_dict()
            else:
                params['ext_params'] = self.ext_params
        if self.item_detail:
            if isinstance(self.item_detail, list):
                for i in range(0, len(self.item_detail)):
                    element = self.item_detail[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_detail[i] = element.to_alipay_dict()
            if hasattr(self.item_detail, 'to_alipay_dict'):
                params['item_detail'] = self.item_detail.to_alipay_dict()
            else:
                params['item_detail'] = self.item_detail
        if self.logistic_status:
            if hasattr(self.logistic_status, 'to_alipay_dict'):
                params['logistic_status'] = self.logistic_status.to_alipay_dict()
            else:
                params['logistic_status'] = self.logistic_status
        if self.order_created_time:
            if hasattr(self.order_created_time, 'to_alipay_dict'):
                params['order_created_time'] = self.order_created_time.to_alipay_dict()
            else:
                params['order_created_time'] = self.order_created_time
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.pay_order_id:
            if hasattr(self.pay_order_id, 'to_alipay_dict'):
                params['pay_order_id'] = self.pay_order_id.to_alipay_dict()
            else:
                params['pay_order_id'] = self.pay_order_id
        if self.pay_status:
            if hasattr(self.pay_status, 'to_alipay_dict'):
                params['pay_status'] = self.pay_status.to_alipay_dict()
            else:
                params['pay_status'] = self.pay_status
        if self.real_amount:
            if hasattr(self.real_amount, 'to_alipay_dict'):
                params['real_amount'] = self.real_amount.to_alipay_dict()
            else:
                params['real_amount'] = self.real_amount
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.seller_open_id:
            if hasattr(self.seller_open_id, 'to_alipay_dict'):
                params['seller_open_id'] = self.seller_open_id.to_alipay_dict()
            else:
                params['seller_open_id'] = self.seller_open_id
        if self.service_type:
            if hasattr(self.service_type, 'to_alipay_dict'):
                params['service_type'] = self.service_type.to_alipay_dict()
            else:
                params['service_type'] = self.service_type
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.subject:
            if hasattr(self.subject, 'to_alipay_dict'):
                params['subject'] = self.subject.to_alipay_dict()
            else:
                params['subject'] = self.subject
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudFundBizOrderCreateModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'biz_industry' in d:
            o.biz_industry = d['biz_industry']
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'buyer_open_id' in d:
            o.buyer_open_id = d['buyer_open_id']
        if 'ext_params' in d:
            o.ext_params = d['ext_params']
        if 'item_detail' in d:
            o.item_detail = d['item_detail']
        if 'logistic_status' in d:
            o.logistic_status = d['logistic_status']
        if 'order_created_time' in d:
            o.order_created_time = d['order_created_time']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'pay_order_id' in d:
            o.pay_order_id = d['pay_order_id']
        if 'pay_status' in d:
            o.pay_status = d['pay_status']
        if 'real_amount' in d:
            o.real_amount = d['real_amount']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'seller_open_id' in d:
            o.seller_open_id = d['seller_open_id']
        if 'service_type' in d:
            o.service_type = d['service_type']
        if 'source' in d:
            o.source = d['source']
        if 'subject' in d:
            o.subject = d['subject']
        return o


