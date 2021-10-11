#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CateringOrderInfo import CateringOrderInfo
from alipay.aop.api.domain.CateringDeliveryInfo import CateringDeliveryInfo
from alipay.aop.api.domain.CateringGoodsInfo import CateringGoodsInfo
from alipay.aop.api.domain.ExtraInfo import ExtraInfo
from alipay.aop.api.domain.PickUpInfo import PickUpInfo
from alipay.aop.api.domain.QueueInfo import QueueInfo
from alipay.aop.api.domain.CateringServiceInfo import CateringServiceInfo


class AlipayCommerceOperationIsvOrderSyncModel(object):

    def __init__(self):
        self._buyer_id = None
        self._catering_order_info = None
        self._delivery_info = None
        self._discount_amount = None
        self._estimate_end_time = None
        self._estimate_start_time = None
        self._goods_info = None
        self._goods_queue_num = None
        self._invoice_url = None
        self._low_carbon_behavior = None
        self._merchant_order_no = None
        self._order_amount = None
        self._order_create_time = None
        self._order_detail_url = None
        self._order_extra_info = None
        self._order_modify_time = None
        self._order_queue_num = None
        self._order_source = None
        self._order_type = None
        self._payment_amount = None
        self._pick_up_info = None
        self._queue_info = None
        self._rebate_pid = None
        self._record_id = None
        self._reorder_url = None
        self._service_code = None
        self._service_info = None
        self._status = None
        self._trade_no = None

    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def catering_order_info(self):
        return self._catering_order_info

    @catering_order_info.setter
    def catering_order_info(self, value):
        if isinstance(value, CateringOrderInfo):
            self._catering_order_info = value
        else:
            self._catering_order_info = CateringOrderInfo.from_alipay_dict(value)
    @property
    def delivery_info(self):
        return self._delivery_info

    @delivery_info.setter
    def delivery_info(self, value):
        if isinstance(value, CateringDeliveryInfo):
            self._delivery_info = value
        else:
            self._delivery_info = CateringDeliveryInfo.from_alipay_dict(value)
    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def estimate_end_time(self):
        return self._estimate_end_time

    @estimate_end_time.setter
    def estimate_end_time(self, value):
        self._estimate_end_time = value
    @property
    def estimate_start_time(self):
        return self._estimate_start_time

    @estimate_start_time.setter
    def estimate_start_time(self, value):
        self._estimate_start_time = value
    @property
    def goods_info(self):
        return self._goods_info

    @goods_info.setter
    def goods_info(self, value):
        if isinstance(value, CateringGoodsInfo):
            self._goods_info = value
        else:
            self._goods_info = CateringGoodsInfo.from_alipay_dict(value)
    @property
    def goods_queue_num(self):
        return self._goods_queue_num

    @goods_queue_num.setter
    def goods_queue_num(self, value):
        self._goods_queue_num = value
    @property
    def invoice_url(self):
        return self._invoice_url

    @invoice_url.setter
    def invoice_url(self, value):
        self._invoice_url = value
    @property
    def low_carbon_behavior(self):
        return self._low_carbon_behavior

    @low_carbon_behavior.setter
    def low_carbon_behavior(self, value):
        self._low_carbon_behavior = value
    @property
    def merchant_order_no(self):
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, value):
        self._merchant_order_no = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def order_create_time(self):
        return self._order_create_time

    @order_create_time.setter
    def order_create_time(self, value):
        self._order_create_time = value
    @property
    def order_detail_url(self):
        return self._order_detail_url

    @order_detail_url.setter
    def order_detail_url(self, value):
        self._order_detail_url = value
    @property
    def order_extra_info(self):
        return self._order_extra_info

    @order_extra_info.setter
    def order_extra_info(self, value):
        if isinstance(value, list):
            self._order_extra_info = list()
            for i in value:
                if isinstance(i, ExtraInfo):
                    self._order_extra_info.append(i)
                else:
                    self._order_extra_info.append(ExtraInfo.from_alipay_dict(i))
    @property
    def order_modify_time(self):
        return self._order_modify_time

    @order_modify_time.setter
    def order_modify_time(self, value):
        self._order_modify_time = value
    @property
    def order_queue_num(self):
        return self._order_queue_num

    @order_queue_num.setter
    def order_queue_num(self, value):
        self._order_queue_num = value
    @property
    def order_source(self):
        return self._order_source

    @order_source.setter
    def order_source(self, value):
        self._order_source = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def payment_amount(self):
        return self._payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        self._payment_amount = value
    @property
    def pick_up_info(self):
        return self._pick_up_info

    @pick_up_info.setter
    def pick_up_info(self, value):
        if isinstance(value, PickUpInfo):
            self._pick_up_info = value
        else:
            self._pick_up_info = PickUpInfo.from_alipay_dict(value)
    @property
    def queue_info(self):
        return self._queue_info

    @queue_info.setter
    def queue_info(self, value):
        if isinstance(value, QueueInfo):
            self._queue_info = value
        else:
            self._queue_info = QueueInfo.from_alipay_dict(value)
    @property
    def rebate_pid(self):
        return self._rebate_pid

    @rebate_pid.setter
    def rebate_pid(self, value):
        self._rebate_pid = value
    @property
    def record_id(self):
        return self._record_id

    @record_id.setter
    def record_id(self, value):
        self._record_id = value
    @property
    def reorder_url(self):
        return self._reorder_url

    @reorder_url.setter
    def reorder_url(self, value):
        self._reorder_url = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value
    @property
    def service_info(self):
        return self._service_info

    @service_info.setter
    def service_info(self, value):
        if isinstance(value, CateringServiceInfo):
            self._service_info = value
        else:
            self._service_info = CateringServiceInfo.from_alipay_dict(value)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.catering_order_info:
            if hasattr(self.catering_order_info, 'to_alipay_dict'):
                params['catering_order_info'] = self.catering_order_info.to_alipay_dict()
            else:
                params['catering_order_info'] = self.catering_order_info
        if self.delivery_info:
            if hasattr(self.delivery_info, 'to_alipay_dict'):
                params['delivery_info'] = self.delivery_info.to_alipay_dict()
            else:
                params['delivery_info'] = self.delivery_info
        if self.discount_amount:
            if hasattr(self.discount_amount, 'to_alipay_dict'):
                params['discount_amount'] = self.discount_amount.to_alipay_dict()
            else:
                params['discount_amount'] = self.discount_amount
        if self.estimate_end_time:
            if hasattr(self.estimate_end_time, 'to_alipay_dict'):
                params['estimate_end_time'] = self.estimate_end_time.to_alipay_dict()
            else:
                params['estimate_end_time'] = self.estimate_end_time
        if self.estimate_start_time:
            if hasattr(self.estimate_start_time, 'to_alipay_dict'):
                params['estimate_start_time'] = self.estimate_start_time.to_alipay_dict()
            else:
                params['estimate_start_time'] = self.estimate_start_time
        if self.goods_info:
            if hasattr(self.goods_info, 'to_alipay_dict'):
                params['goods_info'] = self.goods_info.to_alipay_dict()
            else:
                params['goods_info'] = self.goods_info
        if self.goods_queue_num:
            if hasattr(self.goods_queue_num, 'to_alipay_dict'):
                params['goods_queue_num'] = self.goods_queue_num.to_alipay_dict()
            else:
                params['goods_queue_num'] = self.goods_queue_num
        if self.invoice_url:
            if hasattr(self.invoice_url, 'to_alipay_dict'):
                params['invoice_url'] = self.invoice_url.to_alipay_dict()
            else:
                params['invoice_url'] = self.invoice_url
        if self.low_carbon_behavior:
            if hasattr(self.low_carbon_behavior, 'to_alipay_dict'):
                params['low_carbon_behavior'] = self.low_carbon_behavior.to_alipay_dict()
            else:
                params['low_carbon_behavior'] = self.low_carbon_behavior
        if self.merchant_order_no:
            if hasattr(self.merchant_order_no, 'to_alipay_dict'):
                params['merchant_order_no'] = self.merchant_order_no.to_alipay_dict()
            else:
                params['merchant_order_no'] = self.merchant_order_no
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.order_create_time:
            if hasattr(self.order_create_time, 'to_alipay_dict'):
                params['order_create_time'] = self.order_create_time.to_alipay_dict()
            else:
                params['order_create_time'] = self.order_create_time
        if self.order_detail_url:
            if hasattr(self.order_detail_url, 'to_alipay_dict'):
                params['order_detail_url'] = self.order_detail_url.to_alipay_dict()
            else:
                params['order_detail_url'] = self.order_detail_url
        if self.order_extra_info:
            if isinstance(self.order_extra_info, list):
                for i in range(0, len(self.order_extra_info)):
                    element = self.order_extra_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.order_extra_info[i] = element.to_alipay_dict()
            if hasattr(self.order_extra_info, 'to_alipay_dict'):
                params['order_extra_info'] = self.order_extra_info.to_alipay_dict()
            else:
                params['order_extra_info'] = self.order_extra_info
        if self.order_modify_time:
            if hasattr(self.order_modify_time, 'to_alipay_dict'):
                params['order_modify_time'] = self.order_modify_time.to_alipay_dict()
            else:
                params['order_modify_time'] = self.order_modify_time
        if self.order_queue_num:
            if hasattr(self.order_queue_num, 'to_alipay_dict'):
                params['order_queue_num'] = self.order_queue_num.to_alipay_dict()
            else:
                params['order_queue_num'] = self.order_queue_num
        if self.order_source:
            if hasattr(self.order_source, 'to_alipay_dict'):
                params['order_source'] = self.order_source.to_alipay_dict()
            else:
                params['order_source'] = self.order_source
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.payment_amount:
            if hasattr(self.payment_amount, 'to_alipay_dict'):
                params['payment_amount'] = self.payment_amount.to_alipay_dict()
            else:
                params['payment_amount'] = self.payment_amount
        if self.pick_up_info:
            if hasattr(self.pick_up_info, 'to_alipay_dict'):
                params['pick_up_info'] = self.pick_up_info.to_alipay_dict()
            else:
                params['pick_up_info'] = self.pick_up_info
        if self.queue_info:
            if hasattr(self.queue_info, 'to_alipay_dict'):
                params['queue_info'] = self.queue_info.to_alipay_dict()
            else:
                params['queue_info'] = self.queue_info
        if self.rebate_pid:
            if hasattr(self.rebate_pid, 'to_alipay_dict'):
                params['rebate_pid'] = self.rebate_pid.to_alipay_dict()
            else:
                params['rebate_pid'] = self.rebate_pid
        if self.record_id:
            if hasattr(self.record_id, 'to_alipay_dict'):
                params['record_id'] = self.record_id.to_alipay_dict()
            else:
                params['record_id'] = self.record_id
        if self.reorder_url:
            if hasattr(self.reorder_url, 'to_alipay_dict'):
                params['reorder_url'] = self.reorder_url.to_alipay_dict()
            else:
                params['reorder_url'] = self.reorder_url
        if self.service_code:
            if hasattr(self.service_code, 'to_alipay_dict'):
                params['service_code'] = self.service_code.to_alipay_dict()
            else:
                params['service_code'] = self.service_code
        if self.service_info:
            if hasattr(self.service_info, 'to_alipay_dict'):
                params['service_info'] = self.service_info.to_alipay_dict()
            else:
                params['service_info'] = self.service_info
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceOperationIsvOrderSyncModel()
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'catering_order_info' in d:
            o.catering_order_info = d['catering_order_info']
        if 'delivery_info' in d:
            o.delivery_info = d['delivery_info']
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'estimate_end_time' in d:
            o.estimate_end_time = d['estimate_end_time']
        if 'estimate_start_time' in d:
            o.estimate_start_time = d['estimate_start_time']
        if 'goods_info' in d:
            o.goods_info = d['goods_info']
        if 'goods_queue_num' in d:
            o.goods_queue_num = d['goods_queue_num']
        if 'invoice_url' in d:
            o.invoice_url = d['invoice_url']
        if 'low_carbon_behavior' in d:
            o.low_carbon_behavior = d['low_carbon_behavior']
        if 'merchant_order_no' in d:
            o.merchant_order_no = d['merchant_order_no']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'order_create_time' in d:
            o.order_create_time = d['order_create_time']
        if 'order_detail_url' in d:
            o.order_detail_url = d['order_detail_url']
        if 'order_extra_info' in d:
            o.order_extra_info = d['order_extra_info']
        if 'order_modify_time' in d:
            o.order_modify_time = d['order_modify_time']
        if 'order_queue_num' in d:
            o.order_queue_num = d['order_queue_num']
        if 'order_source' in d:
            o.order_source = d['order_source']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'payment_amount' in d:
            o.payment_amount = d['payment_amount']
        if 'pick_up_info' in d:
            o.pick_up_info = d['pick_up_info']
        if 'queue_info' in d:
            o.queue_info = d['queue_info']
        if 'rebate_pid' in d:
            o.rebate_pid = d['rebate_pid']
        if 'record_id' in d:
            o.record_id = d['record_id']
        if 'reorder_url' in d:
            o.reorder_url = d['reorder_url']
        if 'service_code' in d:
            o.service_code = d['service_code']
        if 'service_info' in d:
            o.service_info = d['service_info']
        if 'status' in d:
            o.status = d['status']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


