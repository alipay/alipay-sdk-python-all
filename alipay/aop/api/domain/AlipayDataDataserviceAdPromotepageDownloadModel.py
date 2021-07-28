#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceAdPromotepageDownloadModel(object):

    def __init__(self):
        self._biz_token = None
        self._end_date = None
        self._page_no = None
        self._page_size = None
        self._principal_tag = None
        self._promote_page_id = None
        self._start_date = None

    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def principal_tag(self):
        return self._principal_tag

    @principal_tag.setter
    def principal_tag(self, value):
        self._principal_tag = value
    @property
    def promote_page_id(self):
        return self._promote_page_id

    @promote_page_id.setter
    def promote_page_id(self, value):
        self._promote_page_id = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_token:
            if hasattr(self.biz_token, 'to_alipay_dict'):
                params['biz_token'] = self.biz_token.to_alipay_dict()
            else:
                params['biz_token'] = self.biz_token
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.page_no:
            if hasattr(self.page_no, 'to_alipay_dict'):
                params['page_no'] = self.page_no.to_alipay_dict()
            else:
                params['page_no'] = self.page_no
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.principal_tag:
            if hasattr(self.principal_tag, 'to_alipay_dict'):
                params['principal_tag'] = self.principal_tag.to_alipay_dict()
            else:
                params['principal_tag'] = self.principal_tag
        if self.promote_page_id:
            if hasattr(self.promote_page_id, 'to_alipay_dict'):
                params['promote_page_id'] = self.promote_page_id.to_alipay_dict()
            else:
                params['promote_page_id'] = self.promote_page_id
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceAdPromotepageDownloadModel()
        if 'biz_token' in d:
            o.biz_token = d['biz_token']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'principal_tag' in d:
            o.principal_tag = d['principal_tag']
        if 'promote_page_id' in d:
            o.promote_page_id = d['promote_page_id']
        if 'start_date' in d:
            o.start_date = d['start_date']
        return o


