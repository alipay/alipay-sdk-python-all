#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SealTabsVO import SealTabsVO


class MultiSignerAndTabVosDTO(object):

    def __init__(self):
        self._email_body = None
        self._email_subject = None
        self._need_emai_notice = None
        self._order = None
        self._recipient_id = None
        self._side = None
        self._signer_email = None
        self._signer_name = None
        self._signer_num = None
        self._supported_language = None
        self._tabs = None

    @property
    def email_body(self):
        return self._email_body

    @email_body.setter
    def email_body(self, value):
        self._email_body = value
    @property
    def email_subject(self):
        return self._email_subject

    @email_subject.setter
    def email_subject(self, value):
        self._email_subject = value
    @property
    def need_emai_notice(self):
        return self._need_emai_notice

    @need_emai_notice.setter
    def need_emai_notice(self, value):
        self._need_emai_notice = value
    @property
    def order(self):
        return self._order

    @order.setter
    def order(self, value):
        self._order = value
    @property
    def recipient_id(self):
        return self._recipient_id

    @recipient_id.setter
    def recipient_id(self, value):
        self._recipient_id = value
    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        self._side = value
    @property
    def signer_email(self):
        return self._signer_email

    @signer_email.setter
    def signer_email(self, value):
        self._signer_email = value
    @property
    def signer_name(self):
        return self._signer_name

    @signer_name.setter
    def signer_name(self, value):
        self._signer_name = value
    @property
    def signer_num(self):
        return self._signer_num

    @signer_num.setter
    def signer_num(self, value):
        self._signer_num = value
    @property
    def supported_language(self):
        return self._supported_language

    @supported_language.setter
    def supported_language(self, value):
        self._supported_language = value
    @property
    def tabs(self):
        return self._tabs

    @tabs.setter
    def tabs(self, value):
        if isinstance(value, list):
            self._tabs = list()
            for i in value:
                if isinstance(i, SealTabsVO):
                    self._tabs.append(i)
                else:
                    self._tabs.append(SealTabsVO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.email_body:
            if hasattr(self.email_body, 'to_alipay_dict'):
                params['email_body'] = self.email_body.to_alipay_dict()
            else:
                params['email_body'] = self.email_body
        if self.email_subject:
            if hasattr(self.email_subject, 'to_alipay_dict'):
                params['email_subject'] = self.email_subject.to_alipay_dict()
            else:
                params['email_subject'] = self.email_subject
        if self.need_emai_notice:
            if hasattr(self.need_emai_notice, 'to_alipay_dict'):
                params['need_emai_notice'] = self.need_emai_notice.to_alipay_dict()
            else:
                params['need_emai_notice'] = self.need_emai_notice
        if self.order:
            if hasattr(self.order, 'to_alipay_dict'):
                params['order'] = self.order.to_alipay_dict()
            else:
                params['order'] = self.order
        if self.recipient_id:
            if hasattr(self.recipient_id, 'to_alipay_dict'):
                params['recipient_id'] = self.recipient_id.to_alipay_dict()
            else:
                params['recipient_id'] = self.recipient_id
        if self.side:
            if hasattr(self.side, 'to_alipay_dict'):
                params['side'] = self.side.to_alipay_dict()
            else:
                params['side'] = self.side
        if self.signer_email:
            if hasattr(self.signer_email, 'to_alipay_dict'):
                params['signer_email'] = self.signer_email.to_alipay_dict()
            else:
                params['signer_email'] = self.signer_email
        if self.signer_name:
            if hasattr(self.signer_name, 'to_alipay_dict'):
                params['signer_name'] = self.signer_name.to_alipay_dict()
            else:
                params['signer_name'] = self.signer_name
        if self.signer_num:
            if hasattr(self.signer_num, 'to_alipay_dict'):
                params['signer_num'] = self.signer_num.to_alipay_dict()
            else:
                params['signer_num'] = self.signer_num
        if self.supported_language:
            if hasattr(self.supported_language, 'to_alipay_dict'):
                params['supported_language'] = self.supported_language.to_alipay_dict()
            else:
                params['supported_language'] = self.supported_language
        if self.tabs:
            if isinstance(self.tabs, list):
                for i in range(0, len(self.tabs)):
                    element = self.tabs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tabs[i] = element.to_alipay_dict()
            if hasattr(self.tabs, 'to_alipay_dict'):
                params['tabs'] = self.tabs.to_alipay_dict()
            else:
                params['tabs'] = self.tabs
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MultiSignerAndTabVosDTO()
        if 'email_body' in d:
            o.email_body = d['email_body']
        if 'email_subject' in d:
            o.email_subject = d['email_subject']
        if 'need_emai_notice' in d:
            o.need_emai_notice = d['need_emai_notice']
        if 'order' in d:
            o.order = d['order']
        if 'recipient_id' in d:
            o.recipient_id = d['recipient_id']
        if 'side' in d:
            o.side = d['side']
        if 'signer_email' in d:
            o.signer_email = d['signer_email']
        if 'signer_name' in d:
            o.signer_name = d['signer_name']
        if 'signer_num' in d:
            o.signer_num = d['signer_num']
        if 'supported_language' in d:
            o.supported_language = d['supported_language']
        if 'tabs' in d:
            o.tabs = d['tabs']
        return o


