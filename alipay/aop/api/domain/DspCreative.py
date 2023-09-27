#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DspAppDownload import DspAppDownload
from alipay.aop.api.domain.DspCreativeElement import DspCreativeElement


class DspCreative(object):

    def __init__(self):
        self._app_download = None
        self._creative_elements = None
        self._creative_id = None
        self._creative_tags = None
        self._deeplink_url = None
        self._end_date = None
        self._start_date = None
        self._target_url = None
        self._template_id = None
        self._trade_id = None

    @property
    def app_download(self):
        return self._app_download

    @app_download.setter
    def app_download(self, value):
        if isinstance(value, list):
            self._app_download = list()
            for i in value:
                if isinstance(i, DspAppDownload):
                    self._app_download.append(i)
                else:
                    self._app_download.append(DspAppDownload.from_alipay_dict(i))
    @property
    def creative_elements(self):
        return self._creative_elements

    @creative_elements.setter
    def creative_elements(self, value):
        if isinstance(value, list):
            self._creative_elements = list()
            for i in value:
                if isinstance(i, DspCreativeElement):
                    self._creative_elements.append(i)
                else:
                    self._creative_elements.append(DspCreativeElement.from_alipay_dict(i))
    @property
    def creative_id(self):
        return self._creative_id

    @creative_id.setter
    def creative_id(self, value):
        self._creative_id = value
    @property
    def creative_tags(self):
        return self._creative_tags

    @creative_tags.setter
    def creative_tags(self, value):
        if isinstance(value, list):
            self._creative_tags = list()
            for i in value:
                self._creative_tags.append(i)
    @property
    def deeplink_url(self):
        return self._deeplink_url

    @deeplink_url.setter
    def deeplink_url(self, value):
        self._deeplink_url = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def target_url(self):
        return self._target_url

    @target_url.setter
    def target_url(self, value):
        self._target_url = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def trade_id(self):
        return self._trade_id

    @trade_id.setter
    def trade_id(self, value):
        self._trade_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_download:
            if isinstance(self.app_download, list):
                for i in range(0, len(self.app_download)):
                    element = self.app_download[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.app_download[i] = element.to_alipay_dict()
            if hasattr(self.app_download, 'to_alipay_dict'):
                params['app_download'] = self.app_download.to_alipay_dict()
            else:
                params['app_download'] = self.app_download
        if self.creative_elements:
            if isinstance(self.creative_elements, list):
                for i in range(0, len(self.creative_elements)):
                    element = self.creative_elements[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.creative_elements[i] = element.to_alipay_dict()
            if hasattr(self.creative_elements, 'to_alipay_dict'):
                params['creative_elements'] = self.creative_elements.to_alipay_dict()
            else:
                params['creative_elements'] = self.creative_elements
        if self.creative_id:
            if hasattr(self.creative_id, 'to_alipay_dict'):
                params['creative_id'] = self.creative_id.to_alipay_dict()
            else:
                params['creative_id'] = self.creative_id
        if self.creative_tags:
            if isinstance(self.creative_tags, list):
                for i in range(0, len(self.creative_tags)):
                    element = self.creative_tags[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.creative_tags[i] = element.to_alipay_dict()
            if hasattr(self.creative_tags, 'to_alipay_dict'):
                params['creative_tags'] = self.creative_tags.to_alipay_dict()
            else:
                params['creative_tags'] = self.creative_tags
        if self.deeplink_url:
            if hasattr(self.deeplink_url, 'to_alipay_dict'):
                params['deeplink_url'] = self.deeplink_url.to_alipay_dict()
            else:
                params['deeplink_url'] = self.deeplink_url
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.target_url:
            if hasattr(self.target_url, 'to_alipay_dict'):
                params['target_url'] = self.target_url.to_alipay_dict()
            else:
                params['target_url'] = self.target_url
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.trade_id:
            if hasattr(self.trade_id, 'to_alipay_dict'):
                params['trade_id'] = self.trade_id.to_alipay_dict()
            else:
                params['trade_id'] = self.trade_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DspCreative()
        if 'app_download' in d:
            o.app_download = d['app_download']
        if 'creative_elements' in d:
            o.creative_elements = d['creative_elements']
        if 'creative_id' in d:
            o.creative_id = d['creative_id']
        if 'creative_tags' in d:
            o.creative_tags = d['creative_tags']
        if 'deeplink_url' in d:
            o.deeplink_url = d['deeplink_url']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'target_url' in d:
            o.target_url = d['target_url']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'trade_id' in d:
            o.trade_id = d['trade_id']
        return o


