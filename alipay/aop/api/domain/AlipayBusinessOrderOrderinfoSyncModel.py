#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Contact import Contact
from alipay.aop.api.domain.ScenicExtInfo import ScenicExtInfo
from alipay.aop.api.domain.Passengers import Passengers
from alipay.aop.api.domain.ScenicTicketInfo import ScenicTicketInfo


class AlipayBusinessOrderOrderinfoSyncModel(object):

    def __init__(self):
        self._amount = None
        self._buyer_id = None
        self._contact = None
        self._discount_amount = None
        self._ext_info = None
        self._order_character = None
        self._order_create_time = None
        self._order_id = None
        self._order_link = None
        self._order_modified_time = None
        self._order_pay_time = None
        self._order_status = None
        self._order_type = None
        self._outer_order_id = None
        self._outer_scenic_id = None
        self._partner_id = None
        self._passengers = None
        self._pay_amount = None
        self._payment_method = None
        self._payment_status = None
        self._refund_amout = None
        self._refund_count = None
        self._refund_fee = None
        self._refund_fee_type = None
        self._refund_status = None
        self._refund_time = None
        self._scenic_app_id = None
        self._source = None
        self._source_system = None
        self._ticket_info = None
        self._trade_no = None
        self._update_msg = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, value):
        if isinstance(value, list):
            self._contact = list()
            for i in value:
                if isinstance(i, Contact):
                    self._contact.append(i)
                else:
                    self._contact.append(Contact.from_alipay_dict(i))
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
        if isinstance(value, list):
            self._ext_info = list()
            for i in value:
                if isinstance(i, ScenicExtInfo):
                    self._ext_info.append(i)
                else:
                    self._ext_info.append(ScenicExtInfo.from_alipay_dict(i))
    @property
    def order_character(self):
        return self._order_character

    @order_character.setter
    def order_character(self, value):
        self._order_character = value
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
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def outer_order_id(self):
        return self._outer_order_id

    @outer_order_id.setter
    def outer_order_id(self, value):
        self._outer_order_id = value
    @property
    def outer_scenic_id(self):
        return self._outer_scenic_id

    @outer_scenic_id.setter
    def outer_scenic_id(self, value):
        self._outer_scenic_id = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def passengers(self):
        return self._passengers

    @passengers.setter
    def passengers(self, value):
        if isinstance(value, list):
            self._passengers = list()
            for i in value:
                if isinstance(i, Passengers):
                    self._passengers.append(i)
                else:
                    self._passengers.append(Passengers.from_alipay_dict(i))
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
    def payment_status(self):
        return self._payment_status

    @payment_status.setter
    def payment_status(self, value):
        self._payment_status = value
    @property
    def refund_amout(self):
        return self._refund_amout

    @refund_amout.setter
    def refund_amout(self, value):
        self._refund_amout = value
    @property
    def refund_count(self):
        return self._refund_count

    @refund_count.setter
    def refund_count(self, value):
        self._refund_count = value
    @property
    def refund_fee(self):
        return self._refund_fee

    @refund_fee.setter
    def refund_fee(self, value):
        self._refund_fee = value
    @property
    def refund_fee_type(self):
        return self._refund_fee_type

    @refund_fee_type.setter
    def refund_fee_type(self, value):
        self._refund_fee_type = value
    @property
    def refund_status(self):
        return self._refund_status

    @refund_status.setter
    def refund_status(self, value):
        self._refund_status = value
    @property
    def refund_time(self):
        return self._refund_time

    @refund_time.setter
    def refund_time(self, value):
        self._refund_time = value
    @property
    def scenic_app_id(self):
        return self._scenic_app_id

    @scenic_app_id.setter
    def scenic_app_id(self, value):
        self._scenic_app_id = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def source_system(self):
        return self._source_system

    @source_system.setter
    def source_system(self, value):
        self._source_system = value
    @property
    def ticket_info(self):
        return self._ticket_info

    @ticket_info.setter
    def ticket_info(self, value):
        if isinstance(value, list):
            self._ticket_info = list()
            for i in value:
                if isinstance(i, ScenicTicketInfo):
                    self._ticket_info.append(i)
                else:
                    self._ticket_info.append(ScenicTicketInfo.from_alipay_dict(i))
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def update_msg(self):
        return self._update_msg

    @update_msg.setter
    def update_msg(self, value):
        self._update_msg = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.contact:
            if isinstance(self.contact, list):
                for i in range(0, len(self.contact)):
                    element = self.contact[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contact[i] = element.to_alipay_dict()
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
            if isinstance(self.ext_info, list):
                for i in range(0, len(self.ext_info)):
                    element = self.ext_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext_info[i] = element.to_alipay_dict()
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.order_character:
            if hasattr(self.order_character, 'to_alipay_dict'):
                params['order_character'] = self.order_character.to_alipay_dict()
            else:
                params['order_character'] = self.order_character
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
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.outer_order_id:
            if hasattr(self.outer_order_id, 'to_alipay_dict'):
                params['outer_order_id'] = self.outer_order_id.to_alipay_dict()
            else:
                params['outer_order_id'] = self.outer_order_id
        if self.outer_scenic_id:
            if hasattr(self.outer_scenic_id, 'to_alipay_dict'):
                params['outer_scenic_id'] = self.outer_scenic_id.to_alipay_dict()
            else:
                params['outer_scenic_id'] = self.outer_scenic_id
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.passengers:
            if isinstance(self.passengers, list):
                for i in range(0, len(self.passengers)):
                    element = self.passengers[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.passengers[i] = element.to_alipay_dict()
            if hasattr(self.passengers, 'to_alipay_dict'):
                params['passengers'] = self.passengers.to_alipay_dict()
            else:
                params['passengers'] = self.passengers
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
        if self.payment_status:
            if hasattr(self.payment_status, 'to_alipay_dict'):
                params['payment_status'] = self.payment_status.to_alipay_dict()
            else:
                params['payment_status'] = self.payment_status
        if self.refund_amout:
            if hasattr(self.refund_amout, 'to_alipay_dict'):
                params['refund_amout'] = self.refund_amout.to_alipay_dict()
            else:
                params['refund_amout'] = self.refund_amout
        if self.refund_count:
            if hasattr(self.refund_count, 'to_alipay_dict'):
                params['refund_count'] = self.refund_count.to_alipay_dict()
            else:
                params['refund_count'] = self.refund_count
        if self.refund_fee:
            if hasattr(self.refund_fee, 'to_alipay_dict'):
                params['refund_fee'] = self.refund_fee.to_alipay_dict()
            else:
                params['refund_fee'] = self.refund_fee
        if self.refund_fee_type:
            if hasattr(self.refund_fee_type, 'to_alipay_dict'):
                params['refund_fee_type'] = self.refund_fee_type.to_alipay_dict()
            else:
                params['refund_fee_type'] = self.refund_fee_type
        if self.refund_status:
            if hasattr(self.refund_status, 'to_alipay_dict'):
                params['refund_status'] = self.refund_status.to_alipay_dict()
            else:
                params['refund_status'] = self.refund_status
        if self.refund_time:
            if hasattr(self.refund_time, 'to_alipay_dict'):
                params['refund_time'] = self.refund_time.to_alipay_dict()
            else:
                params['refund_time'] = self.refund_time
        if self.scenic_app_id:
            if hasattr(self.scenic_app_id, 'to_alipay_dict'):
                params['scenic_app_id'] = self.scenic_app_id.to_alipay_dict()
            else:
                params['scenic_app_id'] = self.scenic_app_id
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.source_system:
            if hasattr(self.source_system, 'to_alipay_dict'):
                params['source_system'] = self.source_system.to_alipay_dict()
            else:
                params['source_system'] = self.source_system
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
        if self.update_msg:
            if hasattr(self.update_msg, 'to_alipay_dict'):
                params['update_msg'] = self.update_msg.to_alipay_dict()
            else:
                params['update_msg'] = self.update_msg
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBusinessOrderOrderinfoSyncModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'contact' in d:
            o.contact = d['contact']
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'order_character' in d:
            o.order_character = d['order_character']
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
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'outer_order_id' in d:
            o.outer_order_id = d['outer_order_id']
        if 'outer_scenic_id' in d:
            o.outer_scenic_id = d['outer_scenic_id']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'passengers' in d:
            o.passengers = d['passengers']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'payment_method' in d:
            o.payment_method = d['payment_method']
        if 'payment_status' in d:
            o.payment_status = d['payment_status']
        if 'refund_amout' in d:
            o.refund_amout = d['refund_amout']
        if 'refund_count' in d:
            o.refund_count = d['refund_count']
        if 'refund_fee' in d:
            o.refund_fee = d['refund_fee']
        if 'refund_fee_type' in d:
            o.refund_fee_type = d['refund_fee_type']
        if 'refund_status' in d:
            o.refund_status = d['refund_status']
        if 'refund_time' in d:
            o.refund_time = d['refund_time']
        if 'scenic_app_id' in d:
            o.scenic_app_id = d['scenic_app_id']
        if 'source' in d:
            o.source = d['source']
        if 'source_system' in d:
            o.source_system = d['source_system']
        if 'ticket_info' in d:
            o.ticket_info = d['ticket_info']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'update_msg' in d:
            o.update_msg = d['update_msg']
        return o


