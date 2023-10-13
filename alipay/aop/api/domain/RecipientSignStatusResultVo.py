#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecipientSignStatusResultVo(object):

    def __init__(self):
        self._creation_reason = None
        self._declined_date_time = None
        self._declined_reason = None
        self._default_recipient = None
        self._delivered_date_time = None
        self._delivery_method = None
        self._docu_name = None
        self._email = None
        self._first_name = None
        self._full_name = None
        self._last_name = None
        self._name = None
        self._nick_name = None
        self._note = None
        self._real_name = None
        self._recipient_id = None
        self._recipient_type = None
        self._routing_order = None
        self._sent_date_time = None
        self._sign_account_no = None
        self._signed_date_time = None
        self._status = None
        self._status_code = None
        self._work_no = None

    @property
    def creation_reason(self):
        return self._creation_reason

    @creation_reason.setter
    def creation_reason(self, value):
        self._creation_reason = value
    @property
    def declined_date_time(self):
        return self._declined_date_time

    @declined_date_time.setter
    def declined_date_time(self, value):
        self._declined_date_time = value
    @property
    def declined_reason(self):
        return self._declined_reason

    @declined_reason.setter
    def declined_reason(self, value):
        self._declined_reason = value
    @property
    def default_recipient(self):
        return self._default_recipient

    @default_recipient.setter
    def default_recipient(self, value):
        self._default_recipient = value
    @property
    def delivered_date_time(self):
        return self._delivered_date_time

    @delivered_date_time.setter
    def delivered_date_time(self, value):
        self._delivered_date_time = value
    @property
    def delivery_method(self):
        return self._delivery_method

    @delivery_method.setter
    def delivery_method(self, value):
        self._delivery_method = value
    @property
    def docu_name(self):
        return self._docu_name

    @docu_name.setter
    def docu_name(self, value):
        self._docu_name = value
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value
    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, value):
        self._full_name = value
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def nick_name(self):
        return self._nick_name

    @nick_name.setter
    def nick_name(self, value):
        self._nick_name = value
    @property
    def note(self):
        return self._note

    @note.setter
    def note(self, value):
        self._note = value
    @property
    def real_name(self):
        return self._real_name

    @real_name.setter
    def real_name(self, value):
        self._real_name = value
    @property
    def recipient_id(self):
        return self._recipient_id

    @recipient_id.setter
    def recipient_id(self, value):
        self._recipient_id = value
    @property
    def recipient_type(self):
        return self._recipient_type

    @recipient_type.setter
    def recipient_type(self, value):
        self._recipient_type = value
    @property
    def routing_order(self):
        return self._routing_order

    @routing_order.setter
    def routing_order(self, value):
        self._routing_order = value
    @property
    def sent_date_time(self):
        return self._sent_date_time

    @sent_date_time.setter
    def sent_date_time(self, value):
        self._sent_date_time = value
    @property
    def sign_account_no(self):
        return self._sign_account_no

    @sign_account_no.setter
    def sign_account_no(self, value):
        self._sign_account_no = value
    @property
    def signed_date_time(self):
        return self._signed_date_time

    @signed_date_time.setter
    def signed_date_time(self, value):
        self._signed_date_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def status_code(self):
        return self._status_code

    @status_code.setter
    def status_code(self, value):
        self._status_code = value
    @property
    def work_no(self):
        return self._work_no

    @work_no.setter
    def work_no(self, value):
        self._work_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.creation_reason:
            if hasattr(self.creation_reason, 'to_alipay_dict'):
                params['creation_reason'] = self.creation_reason.to_alipay_dict()
            else:
                params['creation_reason'] = self.creation_reason
        if self.declined_date_time:
            if hasattr(self.declined_date_time, 'to_alipay_dict'):
                params['declined_date_time'] = self.declined_date_time.to_alipay_dict()
            else:
                params['declined_date_time'] = self.declined_date_time
        if self.declined_reason:
            if hasattr(self.declined_reason, 'to_alipay_dict'):
                params['declined_reason'] = self.declined_reason.to_alipay_dict()
            else:
                params['declined_reason'] = self.declined_reason
        if self.default_recipient:
            if hasattr(self.default_recipient, 'to_alipay_dict'):
                params['default_recipient'] = self.default_recipient.to_alipay_dict()
            else:
                params['default_recipient'] = self.default_recipient
        if self.delivered_date_time:
            if hasattr(self.delivered_date_time, 'to_alipay_dict'):
                params['delivered_date_time'] = self.delivered_date_time.to_alipay_dict()
            else:
                params['delivered_date_time'] = self.delivered_date_time
        if self.delivery_method:
            if hasattr(self.delivery_method, 'to_alipay_dict'):
                params['delivery_method'] = self.delivery_method.to_alipay_dict()
            else:
                params['delivery_method'] = self.delivery_method
        if self.docu_name:
            if hasattr(self.docu_name, 'to_alipay_dict'):
                params['docu_name'] = self.docu_name.to_alipay_dict()
            else:
                params['docu_name'] = self.docu_name
        if self.email:
            if hasattr(self.email, 'to_alipay_dict'):
                params['email'] = self.email.to_alipay_dict()
            else:
                params['email'] = self.email
        if self.first_name:
            if hasattr(self.first_name, 'to_alipay_dict'):
                params['first_name'] = self.first_name.to_alipay_dict()
            else:
                params['first_name'] = self.first_name
        if self.full_name:
            if hasattr(self.full_name, 'to_alipay_dict'):
                params['full_name'] = self.full_name.to_alipay_dict()
            else:
                params['full_name'] = self.full_name
        if self.last_name:
            if hasattr(self.last_name, 'to_alipay_dict'):
                params['last_name'] = self.last_name.to_alipay_dict()
            else:
                params['last_name'] = self.last_name
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.nick_name:
            if hasattr(self.nick_name, 'to_alipay_dict'):
                params['nick_name'] = self.nick_name.to_alipay_dict()
            else:
                params['nick_name'] = self.nick_name
        if self.note:
            if hasattr(self.note, 'to_alipay_dict'):
                params['note'] = self.note.to_alipay_dict()
            else:
                params['note'] = self.note
        if self.real_name:
            if hasattr(self.real_name, 'to_alipay_dict'):
                params['real_name'] = self.real_name.to_alipay_dict()
            else:
                params['real_name'] = self.real_name
        if self.recipient_id:
            if hasattr(self.recipient_id, 'to_alipay_dict'):
                params['recipient_id'] = self.recipient_id.to_alipay_dict()
            else:
                params['recipient_id'] = self.recipient_id
        if self.recipient_type:
            if hasattr(self.recipient_type, 'to_alipay_dict'):
                params['recipient_type'] = self.recipient_type.to_alipay_dict()
            else:
                params['recipient_type'] = self.recipient_type
        if self.routing_order:
            if hasattr(self.routing_order, 'to_alipay_dict'):
                params['routing_order'] = self.routing_order.to_alipay_dict()
            else:
                params['routing_order'] = self.routing_order
        if self.sent_date_time:
            if hasattr(self.sent_date_time, 'to_alipay_dict'):
                params['sent_date_time'] = self.sent_date_time.to_alipay_dict()
            else:
                params['sent_date_time'] = self.sent_date_time
        if self.sign_account_no:
            if hasattr(self.sign_account_no, 'to_alipay_dict'):
                params['sign_account_no'] = self.sign_account_no.to_alipay_dict()
            else:
                params['sign_account_no'] = self.sign_account_no
        if self.signed_date_time:
            if hasattr(self.signed_date_time, 'to_alipay_dict'):
                params['signed_date_time'] = self.signed_date_time.to_alipay_dict()
            else:
                params['signed_date_time'] = self.signed_date_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.status_code:
            if hasattr(self.status_code, 'to_alipay_dict'):
                params['status_code'] = self.status_code.to_alipay_dict()
            else:
                params['status_code'] = self.status_code
        if self.work_no:
            if hasattr(self.work_no, 'to_alipay_dict'):
                params['work_no'] = self.work_no.to_alipay_dict()
            else:
                params['work_no'] = self.work_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecipientSignStatusResultVo()
        if 'creation_reason' in d:
            o.creation_reason = d['creation_reason']
        if 'declined_date_time' in d:
            o.declined_date_time = d['declined_date_time']
        if 'declined_reason' in d:
            o.declined_reason = d['declined_reason']
        if 'default_recipient' in d:
            o.default_recipient = d['default_recipient']
        if 'delivered_date_time' in d:
            o.delivered_date_time = d['delivered_date_time']
        if 'delivery_method' in d:
            o.delivery_method = d['delivery_method']
        if 'docu_name' in d:
            o.docu_name = d['docu_name']
        if 'email' in d:
            o.email = d['email']
        if 'first_name' in d:
            o.first_name = d['first_name']
        if 'full_name' in d:
            o.full_name = d['full_name']
        if 'last_name' in d:
            o.last_name = d['last_name']
        if 'name' in d:
            o.name = d['name']
        if 'nick_name' in d:
            o.nick_name = d['nick_name']
        if 'note' in d:
            o.note = d['note']
        if 'real_name' in d:
            o.real_name = d['real_name']
        if 'recipient_id' in d:
            o.recipient_id = d['recipient_id']
        if 'recipient_type' in d:
            o.recipient_type = d['recipient_type']
        if 'routing_order' in d:
            o.routing_order = d['routing_order']
        if 'sent_date_time' in d:
            o.sent_date_time = d['sent_date_time']
        if 'sign_account_no' in d:
            o.sign_account_no = d['sign_account_no']
        if 'signed_date_time' in d:
            o.signed_date_time = d['signed_date_time']
        if 'status' in d:
            o.status = d['status']
        if 'status_code' in d:
            o.status_code = d['status_code']
        if 'work_no' in d:
            o.work_no = d['work_no']
        return o


