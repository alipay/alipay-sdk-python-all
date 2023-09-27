#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceSportsTicketSendModel(object):

    def __init__(self):
        self._biz_no = None
        self._city_code = None
        self._discipline = None
        self._discipline_en = None
        self._end_time = None
        self._ext_info = None
        self._send_time = None
        self._source = None
        self._start_time = None
        self._user_id = None
        self._user_open_id = None
        self._venue_id = None
        self._venue_name = None
        self._venue_name_en = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def discipline(self):
        return self._discipline

    @discipline.setter
    def discipline(self, value):
        self._discipline = value
    @property
    def discipline_en(self):
        return self._discipline_en

    @discipline_en.setter
    def discipline_en(self, value):
        self._discipline_en = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def send_time(self):
        return self._send_time

    @send_time.setter
    def send_time(self, value):
        self._send_time = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_open_id(self):
        return self._user_open_id

    @user_open_id.setter
    def user_open_id(self, value):
        self._user_open_id = value
    @property
    def venue_id(self):
        return self._venue_id

    @venue_id.setter
    def venue_id(self, value):
        self._venue_id = value
    @property
    def venue_name(self):
        return self._venue_name

    @venue_name.setter
    def venue_name(self, value):
        self._venue_name = value
    @property
    def venue_name_en(self):
        return self._venue_name_en

    @venue_name_en.setter
    def venue_name_en(self, value):
        self._venue_name_en = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.discipline:
            if hasattr(self.discipline, 'to_alipay_dict'):
                params['discipline'] = self.discipline.to_alipay_dict()
            else:
                params['discipline'] = self.discipline
        if self.discipline_en:
            if hasattr(self.discipline_en, 'to_alipay_dict'):
                params['discipline_en'] = self.discipline_en.to_alipay_dict()
            else:
                params['discipline_en'] = self.discipline_en
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.send_time:
            if hasattr(self.send_time, 'to_alipay_dict'):
                params['send_time'] = self.send_time.to_alipay_dict()
            else:
                params['send_time'] = self.send_time
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_open_id:
            if hasattr(self.user_open_id, 'to_alipay_dict'):
                params['user_open_id'] = self.user_open_id.to_alipay_dict()
            else:
                params['user_open_id'] = self.user_open_id
        if self.venue_id:
            if hasattr(self.venue_id, 'to_alipay_dict'):
                params['venue_id'] = self.venue_id.to_alipay_dict()
            else:
                params['venue_id'] = self.venue_id
        if self.venue_name:
            if hasattr(self.venue_name, 'to_alipay_dict'):
                params['venue_name'] = self.venue_name.to_alipay_dict()
            else:
                params['venue_name'] = self.venue_name
        if self.venue_name_en:
            if hasattr(self.venue_name_en, 'to_alipay_dict'):
                params['venue_name_en'] = self.venue_name_en.to_alipay_dict()
            else:
                params['venue_name_en'] = self.venue_name_en
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceSportsTicketSendModel()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'discipline' in d:
            o.discipline = d['discipline']
        if 'discipline_en' in d:
            o.discipline_en = d['discipline_en']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'send_time' in d:
            o.send_time = d['send_time']
        if 'source' in d:
            o.source = d['source']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_open_id' in d:
            o.user_open_id = d['user_open_id']
        if 'venue_id' in d:
            o.venue_id = d['venue_id']
        if 'venue_name' in d:
            o.venue_name = d['venue_name']
        if 'venue_name_en' in d:
            o.venue_name_en = d['venue_name_en']
        return o


