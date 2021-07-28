#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserFamilyArchiveInitializeModel(object):

    def __init__(self):
        self._archive_id_list = None
        self._max_archives_cnt = None
        self._min_archives_cnt = None
        self._out_biz_no = None
        self._redirect_uri = None
        self._template_id = None

    @property
    def archive_id_list(self):
        return self._archive_id_list

    @archive_id_list.setter
    def archive_id_list(self, value):
        if isinstance(value, list):
            self._archive_id_list = list()
            for i in value:
                self._archive_id_list.append(i)
    @property
    def max_archives_cnt(self):
        return self._max_archives_cnt

    @max_archives_cnt.setter
    def max_archives_cnt(self, value):
        self._max_archives_cnt = value
    @property
    def min_archives_cnt(self):
        return self._min_archives_cnt

    @min_archives_cnt.setter
    def min_archives_cnt(self, value):
        self._min_archives_cnt = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def redirect_uri(self):
        return self._redirect_uri

    @redirect_uri.setter
    def redirect_uri(self, value):
        self._redirect_uri = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.archive_id_list:
            if isinstance(self.archive_id_list, list):
                for i in range(0, len(self.archive_id_list)):
                    element = self.archive_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.archive_id_list[i] = element.to_alipay_dict()
            if hasattr(self.archive_id_list, 'to_alipay_dict'):
                params['archive_id_list'] = self.archive_id_list.to_alipay_dict()
            else:
                params['archive_id_list'] = self.archive_id_list
        if self.max_archives_cnt:
            if hasattr(self.max_archives_cnt, 'to_alipay_dict'):
                params['max_archives_cnt'] = self.max_archives_cnt.to_alipay_dict()
            else:
                params['max_archives_cnt'] = self.max_archives_cnt
        if self.min_archives_cnt:
            if hasattr(self.min_archives_cnt, 'to_alipay_dict'):
                params['min_archives_cnt'] = self.min_archives_cnt.to_alipay_dict()
            else:
                params['min_archives_cnt'] = self.min_archives_cnt
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.redirect_uri:
            if hasattr(self.redirect_uri, 'to_alipay_dict'):
                params['redirect_uri'] = self.redirect_uri.to_alipay_dict()
            else:
                params['redirect_uri'] = self.redirect_uri
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserFamilyArchiveInitializeModel()
        if 'archive_id_list' in d:
            o.archive_id_list = d['archive_id_list']
        if 'max_archives_cnt' in d:
            o.max_archives_cnt = d['max_archives_cnt']
        if 'min_archives_cnt' in d:
            o.min_archives_cnt = d['min_archives_cnt']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'redirect_uri' in d:
            o.redirect_uri = d['redirect_uri']
        if 'template_id' in d:
            o.template_id = d['template_id']
        return o


