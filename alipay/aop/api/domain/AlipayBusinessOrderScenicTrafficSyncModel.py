#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ScenicTrafficUserInfo import ScenicTrafficUserInfo
from alipay.aop.api.domain.ScenicExtInfo import ScenicExtInfo
from alipay.aop.api.domain.ScenicTrafficTicketInfo import ScenicTrafficTicketInfo


class AlipayBusinessOrderScenicTrafficSyncModel(object):

    def __init__(self):
        self._amount = None
        self._app_name = None
        self._appid = None
        self._contact = None
        self._discount_amount = None
        self._ext_info = None
        self._order_create_time = None
        self._order_id = None
        self._order_link = None
        self._order_modified_time = None
        self._order_pay_time = None
        self._order_source = None
        self._order_status = None
        self._outer_order_id = None
        self._pay_amount = None
        self._payment_method = None
        self._refund_amount = None
        self._refund_status = None
        self._refund_ticket_num = None
        self._refund_time = None
        self._ticket_info = None
        self._trade_no = None
        self._uid = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def appid(self):
        return self._appid

    @appid.setter
    def appid(self, value):
        self._appid = value
    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, value):
        if isinstance(value, ScenicTrafficUserInfo):
            self._contact = value
        else:
            self._contact = ScenicTrafficUserInfo.from_alipay_dict(value)
    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, ScenicExtInfo):
            self._ext_info = value
        else:
            self._ext_info = ScenicExtInfo.from_alipay_dict(value)
    @property
    def order_create_time(self):
        return self._order_create_time

    @order_create_time.setter
    def order_create_time(self, value):
        self._order_create_time = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_link(self):
        return self._order_link

    @order_link.setter
    def order_link(self, value):
        self._order_link = value
    @property
    def order_modified_time(self):
        return self._order_modified_time

    @order_modified_time.setter
    def order_modified_time(self, value):
        self._order_modified_time = value
    @property
    def order_pay_time(self):
        return self._order_pay_time

    @order_pay_time.setter
    def order_pay_time(self, value):
        self._order_pay_time = value
    @property
    def order_source(self):
        return self._order_source

    @order_source.setter
    def order_source(self, value):
        self._order_source = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def outer_order_id(self):
        return self._outer_order_id

    @outer_order_id.setter
    def outer_order_id(self, value):
        self._outer_order_id = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def payment_method(self):
        return self._payment_method

    @payment_method.setter
    def payment_method(self, value):
        self._payment_method = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_status(self):
        return self._refund_status

    @refund_status.setter
    def refund_status(self, value):
        self._refund_status = value
    @property
    def refund_ticket_num(self):
        return self._refund_ticket_num

    @refund_ticket_num.setter
    def refund_ticket_num(self, value):
        self._refund_ticket_num = value
    @property
    def refund_time(self):
        return self._refund_time

    @refund_time.setter
    def refund_time(self, value):
        self._refund_time = value
    @property
    def ticket_info(self):
        return self._ticket_info

    @ticket_info.setter
    def ticket_info(self, value):
        if isinstance(value, list):
            self._ticket_info = list()
            for i in value:
                if isinstance(i, ScenicTrafficTicketInfo):
                    self._ticket_info.append(i)
                else:
                    self._ticket_info.append(ScenicTrafficTicketInfo.from_alipay_dict(i))
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.appid:
            if hasattr(self.appid, 'to_alipay_dict'):
                params['appid'] = self.appid.to_alipay_dict()
            else:
                params['appid'] = self.appid
        if self.contact:
            if hasattr(self.contact, 'to_alipay_dict'):
                params['contact'] = self.contact.to_alipay_dict()
            else:
                params['contact'] = self.contact
        if self.discount_amount:
            if hasattr(self.discount_amount, 'to_alipay_dict'):
                params['discount_amount'] = self.discount_amount.to_alipay_dict()
            else:
                params['discount_amount'] = self.discount_amount
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.order_create_time:
            if hasattr(self.order_create_time, 'to_alipay_dict'):
                params['order_create_time'] = self.order_create_time.to_alipay_dict()
            else:
                params['order_create_time'] = self.order_create_time
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_link:
            if hasattr(self.order_link, 'to_alipay_dict'):
                params['order_link'] = self.order_link.to_alipay_dict()
            else:
                params['order_link'] = self.order_link
        if self.order_modified_time:
            if hasattr(self.order_modified_time, 'to_alipay_dict'):
                params['order_modified_time'] = self.order_modified_time.to_alipay_dict()
            else:
                params['order_modified_time'] = self.order_modified_time
        if self.order_pay_time:
            if hasattr(self.order_pay_time, 'to_alipay_dict'):
                params['order_pay_time'] = self.order_pay_time.to_alipay_dict()
            else:
                params['order_pay_time'] = self.order_pay_time
        if self.order_source:
            if hasattr(self.order_source, 'to_alipay_dict'):
                params['order_source'] = self.order_source.to_alipay_dict()
            else:
                params['order_source'] = self.order_source
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.outer_order_id:
            if hasattr(self.outer_order_id, 'to_alipay_dict'):
                params['outer_order_id'] = self.outer_order_id.to_alipay_dict()
            else:
                params['outer_order_id'] = self.outer_order_id
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.payment_method:
            if hasattr(self.payment_method, 'to_alipay_dict'):
                params['payment_method'] = self.payment_method.to_alipay_dict()
            else:
                params['payment_method'] = self.payment_method
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_status:
            if hasattr(self.refund_status, 'to_alipay_dict'):
                params['refund_status'] = self.refund_status.to_alipay_dict()
            else:
                params['refund_status'] = self.refund_status
        if self.refund_ticket_num:
            if hasattr(self.refund_ticket_num, 'to_alipay_dict'):
                params['refund_ticket_num'] = self.refund_ticket_num.to_alipay_dict()
            else:
                params['refund_ticket_num'] = self.refund_ticket_num
        if self.refund_time:
            if hasattr(self.refund_time, 'to_alipay_dict'):
                params['refund_time'] = self.refund_time.to_alipay_dict()
            else:
                params['refund_time'] = self.refund_time
        if self.ticket_info:
            if isinstance(self.ticket_info, list):
                for i in range(0, len(self.ticket_info)):
                    element = self.ticket_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ticket_info[i] = element.to_alipay_dict()
            if hasattr(self.ticket_info, 'to_alipay_dict'):
                params['ticket_info'] = self.ticket_info.to_alipay_dict()
            else:
                params['ticket_info'] = self.ticket_info
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.uid:
            if hasattr(self.uid, 'to_alipay_dict'):
                params['uid'] = self.uid.to_alipay_dict()
            else:
                params['uid'] = self.uid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBusinessOrderScenicTrafficSyncModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'appid' in d:
            o.appid = d['appid']
        if 'contact' in d:
            o.contact = d['contact']
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'order_create_time' in d:
            o.order_create_time = d['order_create_time']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_link' in d:
            o.order_link = d['order_link']
        if 'order_modified_time' in d:
            o.order_modified_time = d['order_modified_time']
        if 'order_pay_time' in d:
            o.order_pay_time = d['order_pay_time']
        if 'order_source' in d:
            o.order_source = d['order_source']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'outer_order_id' in d:
            o.outer_order_id = d['outer_order_id']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'payment_method' in d:
            o.payment_method = d['payment_method']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_status' in d:
            o.refund_status = d['refund_status']
        if 'refund_ticket_num' in d:
            o.refund_ticket_num = d['refund_ticket_num']
        if 'refund_time' in d:
            o.refund_time = d['refund_time']
        if 'ticket_info' in d:
            o.ticket_info = d['ticket_info']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'uid' in d:
            o.uid = d['uid']
        return o


