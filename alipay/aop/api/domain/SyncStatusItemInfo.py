#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SyncStatusItemInfo(object):

    def __init__(self):
        self._appointment_end_time = None
        self._appointment_start_time = None
        self._image_type = None
        self._image_url = None
        self._item_code = None
        self._item_name = None
        self._item_status = None
        self._pdf_url = None
        self._report_time = None

    @property
    def appointment_end_time(self):
        return self._appointment_end_time

    @appointment_end_time.setter
    def appointment_end_time(self, value):
        self._appointment_end_time = value
    @property
    def appointment_start_time(self):
        return self._appointment_start_time

    @appointment_start_time.setter
    def appointment_start_time(self, value):
        self._appointment_start_time = value
    @property
    def image_type(self):
        return self._image_type

    @image_type.setter
    def image_type(self, value):
        self._image_type = value
    @property
    def image_url(self):
        return self._image_url

    @image_url.setter
    def image_url(self, value):
        self._image_url = value
    @property
    def item_code(self):
        return self._item_code

    @item_code.setter
    def item_code(self, value):
        self._item_code = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def item_status(self):
        return self._item_status

    @item_status.setter
    def item_status(self, value):
        self._item_status = value
    @property
    def pdf_url(self):
        return self._pdf_url

    @pdf_url.setter
    def pdf_url(self, value):
        self._pdf_url = value
    @property
    def report_time(self):
        return self._report_time

    @report_time.setter
    def report_time(self, value):
        self._report_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.appointment_end_time:
            if hasattr(self.appointment_end_time, 'to_alipay_dict'):
                params['appointment_end_time'] = self.appointment_end_time.to_alipay_dict()
            else:
                params['appointment_end_time'] = self.appointment_end_time
        if self.appointment_start_time:
            if hasattr(self.appointment_start_time, 'to_alipay_dict'):
                params['appointment_start_time'] = self.appointment_start_time.to_alipay_dict()
            else:
                params['appointment_start_time'] = self.appointment_start_time
        if self.image_type:
            if hasattr(self.image_type, 'to_alipay_dict'):
                params['image_type'] = self.image_type.to_alipay_dict()
            else:
                params['image_type'] = self.image_type
        if self.image_url:
            if hasattr(self.image_url, 'to_alipay_dict'):
                params['image_url'] = self.image_url.to_alipay_dict()
            else:
                params['image_url'] = self.image_url
        if self.item_code:
            if hasattr(self.item_code, 'to_alipay_dict'):
                params['item_code'] = self.item_code.to_alipay_dict()
            else:
                params['item_code'] = self.item_code
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.item_status:
            if hasattr(self.item_status, 'to_alipay_dict'):
                params['item_status'] = self.item_status.to_alipay_dict()
            else:
                params['item_status'] = self.item_status
        if self.pdf_url:
            if hasattr(self.pdf_url, 'to_alipay_dict'):
                params['pdf_url'] = self.pdf_url.to_alipay_dict()
            else:
                params['pdf_url'] = self.pdf_url
        if self.report_time:
            if hasattr(self.report_time, 'to_alipay_dict'):
                params['report_time'] = self.report_time.to_alipay_dict()
            else:
                params['report_time'] = self.report_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SyncStatusItemInfo()
        if 'appointment_end_time' in d:
            o.appointment_end_time = d['appointment_end_time']
        if 'appointment_start_time' in d:
            o.appointment_start_time = d['appointment_start_time']
        if 'image_type' in d:
            o.image_type = d['image_type']
        if 'image_url' in d:
            o.image_url = d['image_url']
        if 'item_code' in d:
            o.item_code = d['item_code']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'item_status' in d:
            o.item_status = d['item_status']
        if 'pdf_url' in d:
            o.pdf_url = d['pdf_url']
        if 'report_time' in d:
            o.report_time = d['report_time']
        return o


