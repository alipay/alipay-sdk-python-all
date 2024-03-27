#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDigitalmgmtHrhealthEntryUserSyncModel(object):

    def __init__(self):
        self._agency_name = None
        self._cert_genre = None
        self._cert_no = None
        self._city_name = None
        self._data_key = None
        self._form_no = None
        self._package_name = None
        self._report_link = None
        self._reservation_status = None
        self._reservation_time = None

    @property
    def agency_name(self):
        return self._agency_name

    @agency_name.setter
    def agency_name(self, value):
        self._agency_name = value
    @property
    def cert_genre(self):
        return self._cert_genre

    @cert_genre.setter
    def cert_genre(self, value):
        self._cert_genre = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def data_key(self):
        return self._data_key

    @data_key.setter
    def data_key(self, value):
        self._data_key = value
    @property
    def form_no(self):
        return self._form_no

    @form_no.setter
    def form_no(self, value):
        self._form_no = value
    @property
    def package_name(self):
        return self._package_name

    @package_name.setter
    def package_name(self, value):
        self._package_name = value
    @property
    def report_link(self):
        return self._report_link

    @report_link.setter
    def report_link(self, value):
        self._report_link = value
    @property
    def reservation_status(self):
        return self._reservation_status

    @reservation_status.setter
    def reservation_status(self, value):
        self._reservation_status = value
    @property
    def reservation_time(self):
        return self._reservation_time

    @reservation_time.setter
    def reservation_time(self, value):
        self._reservation_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.agency_name:
            if hasattr(self.agency_name, 'to_alipay_dict'):
                params['agency_name'] = self.agency_name.to_alipay_dict()
            else:
                params['agency_name'] = self.agency_name
        if self.cert_genre:
            if hasattr(self.cert_genre, 'to_alipay_dict'):
                params['cert_genre'] = self.cert_genre.to_alipay_dict()
            else:
                params['cert_genre'] = self.cert_genre
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.data_key:
            if hasattr(self.data_key, 'to_alipay_dict'):
                params['data_key'] = self.data_key.to_alipay_dict()
            else:
                params['data_key'] = self.data_key
        if self.form_no:
            if hasattr(self.form_no, 'to_alipay_dict'):
                params['form_no'] = self.form_no.to_alipay_dict()
            else:
                params['form_no'] = self.form_no
        if self.package_name:
            if hasattr(self.package_name, 'to_alipay_dict'):
                params['package_name'] = self.package_name.to_alipay_dict()
            else:
                params['package_name'] = self.package_name
        if self.report_link:
            if hasattr(self.report_link, 'to_alipay_dict'):
                params['report_link'] = self.report_link.to_alipay_dict()
            else:
                params['report_link'] = self.report_link
        if self.reservation_status:
            if hasattr(self.reservation_status, 'to_alipay_dict'):
                params['reservation_status'] = self.reservation_status.to_alipay_dict()
            else:
                params['reservation_status'] = self.reservation_status
        if self.reservation_time:
            if hasattr(self.reservation_time, 'to_alipay_dict'):
                params['reservation_time'] = self.reservation_time.to_alipay_dict()
            else:
                params['reservation_time'] = self.reservation_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDigitalmgmtHrhealthEntryUserSyncModel()
        if 'agency_name' in d:
            o.agency_name = d['agency_name']
        if 'cert_genre' in d:
            o.cert_genre = d['cert_genre']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'data_key' in d:
            o.data_key = d['data_key']
        if 'form_no' in d:
            o.form_no = d['form_no']
        if 'package_name' in d:
            o.package_name = d['package_name']
        if 'report_link' in d:
            o.report_link = d['report_link']
        if 'reservation_status' in d:
            o.reservation_status = d['reservation_status']
        if 'reservation_time' in d:
            o.reservation_time = d['reservation_time']
        return o


