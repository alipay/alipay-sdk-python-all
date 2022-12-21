#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CardNumberVO(object):

    def __init__(self):
        self._card_template_id = None
        self._count = None
        self._name = None
        self._pi_url = None
        self._pi_url_dis = None
        self._selected_count = None
        self._serial = None

    @property
    def card_template_id(self):
        return self._card_template_id

    @card_template_id.setter
    def card_template_id(self, value):
        self._card_template_id = value
    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def pi_url(self):
        return self._pi_url

    @pi_url.setter
    def pi_url(self, value):
        self._pi_url = value
    @property
    def pi_url_dis(self):
        return self._pi_url_dis

    @pi_url_dis.setter
    def pi_url_dis(self, value):
        self._pi_url_dis = value
    @property
    def selected_count(self):
        return self._selected_count

    @selected_count.setter
    def selected_count(self, value):
        self._selected_count = value
    @property
    def serial(self):
        return self._serial

    @serial.setter
    def serial(self, value):
        self._serial = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_template_id:
            if hasattr(self.card_template_id, 'to_alipay_dict'):
                params['card_template_id'] = self.card_template_id.to_alipay_dict()
            else:
                params['card_template_id'] = self.card_template_id
        if self.count:
            if hasattr(self.count, 'to_alipay_dict'):
                params['count'] = self.count.to_alipay_dict()
            else:
                params['count'] = self.count
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.pi_url:
            if hasattr(self.pi_url, 'to_alipay_dict'):
                params['pi_url'] = self.pi_url.to_alipay_dict()
            else:
                params['pi_url'] = self.pi_url
        if self.pi_url_dis:
            if hasattr(self.pi_url_dis, 'to_alipay_dict'):
                params['pi_url_dis'] = self.pi_url_dis.to_alipay_dict()
            else:
                params['pi_url_dis'] = self.pi_url_dis
        if self.selected_count:
            if hasattr(self.selected_count, 'to_alipay_dict'):
                params['selected_count'] = self.selected_count.to_alipay_dict()
            else:
                params['selected_count'] = self.selected_count
        if self.serial:
            if hasattr(self.serial, 'to_alipay_dict'):
                params['serial'] = self.serial.to_alipay_dict()
            else:
                params['serial'] = self.serial
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CardNumberVO()
        if 'card_template_id' in d:
            o.card_template_id = d['card_template_id']
        if 'count' in d:
            o.count = d['count']
        if 'name' in d:
            o.name = d['name']
        if 'pi_url' in d:
            o.pi_url = d['pi_url']
        if 'pi_url_dis' in d:
            o.pi_url_dis = d['pi_url_dis']
        if 'selected_count' in d:
            o.selected_count = d['selected_count']
        if 'serial' in d:
            o.serial = d['serial']
        return o


