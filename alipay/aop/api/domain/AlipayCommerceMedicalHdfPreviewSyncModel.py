#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHdfPreviewSyncModel(object):

    def __init__(self):
        self._alipay_public_id = None
        self._out_action = None
        self._out_cover_img = None
        self._out_doc_app_url = None
        self._out_doc_id = None
        self._out_live_time = None
        self._out_prepare_id = None
        self._out_title = None

    @property
    def alipay_public_id(self):
        return self._alipay_public_id

    @alipay_public_id.setter
    def alipay_public_id(self, value):
        self._alipay_public_id = value
    @property
    def out_action(self):
        return self._out_action

    @out_action.setter
    def out_action(self, value):
        self._out_action = value
    @property
    def out_cover_img(self):
        return self._out_cover_img

    @out_cover_img.setter
    def out_cover_img(self, value):
        self._out_cover_img = value
    @property
    def out_doc_app_url(self):
        return self._out_doc_app_url

    @out_doc_app_url.setter
    def out_doc_app_url(self, value):
        self._out_doc_app_url = value
    @property
    def out_doc_id(self):
        return self._out_doc_id

    @out_doc_id.setter
    def out_doc_id(self, value):
        self._out_doc_id = value
    @property
    def out_live_time(self):
        return self._out_live_time

    @out_live_time.setter
    def out_live_time(self, value):
        self._out_live_time = value
    @property
    def out_prepare_id(self):
        return self._out_prepare_id

    @out_prepare_id.setter
    def out_prepare_id(self, value):
        self._out_prepare_id = value
    @property
    def out_title(self):
        return self._out_title

    @out_title.setter
    def out_title(self, value):
        self._out_title = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_public_id:
            if hasattr(self.alipay_public_id, 'to_alipay_dict'):
                params['alipay_public_id'] = self.alipay_public_id.to_alipay_dict()
            else:
                params['alipay_public_id'] = self.alipay_public_id
        if self.out_action:
            if hasattr(self.out_action, 'to_alipay_dict'):
                params['out_action'] = self.out_action.to_alipay_dict()
            else:
                params['out_action'] = self.out_action
        if self.out_cover_img:
            if hasattr(self.out_cover_img, 'to_alipay_dict'):
                params['out_cover_img'] = self.out_cover_img.to_alipay_dict()
            else:
                params['out_cover_img'] = self.out_cover_img
        if self.out_doc_app_url:
            if hasattr(self.out_doc_app_url, 'to_alipay_dict'):
                params['out_doc_app_url'] = self.out_doc_app_url.to_alipay_dict()
            else:
                params['out_doc_app_url'] = self.out_doc_app_url
        if self.out_doc_id:
            if hasattr(self.out_doc_id, 'to_alipay_dict'):
                params['out_doc_id'] = self.out_doc_id.to_alipay_dict()
            else:
                params['out_doc_id'] = self.out_doc_id
        if self.out_live_time:
            if hasattr(self.out_live_time, 'to_alipay_dict'):
                params['out_live_time'] = self.out_live_time.to_alipay_dict()
            else:
                params['out_live_time'] = self.out_live_time
        if self.out_prepare_id:
            if hasattr(self.out_prepare_id, 'to_alipay_dict'):
                params['out_prepare_id'] = self.out_prepare_id.to_alipay_dict()
            else:
                params['out_prepare_id'] = self.out_prepare_id
        if self.out_title:
            if hasattr(self.out_title, 'to_alipay_dict'):
                params['out_title'] = self.out_title.to_alipay_dict()
            else:
                params['out_title'] = self.out_title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHdfPreviewSyncModel()
        if 'alipay_public_id' in d:
            o.alipay_public_id = d['alipay_public_id']
        if 'out_action' in d:
            o.out_action = d['out_action']
        if 'out_cover_img' in d:
            o.out_cover_img = d['out_cover_img']
        if 'out_doc_app_url' in d:
            o.out_doc_app_url = d['out_doc_app_url']
        if 'out_doc_id' in d:
            o.out_doc_id = d['out_doc_id']
        if 'out_live_time' in d:
            o.out_live_time = d['out_live_time']
        if 'out_prepare_id' in d:
            o.out_prepare_id = d['out_prepare_id']
        if 'out_title' in d:
            o.out_title = d['out_title']
        return o


