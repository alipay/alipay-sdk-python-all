#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SelectedSealPosition import SelectedSealPosition
from alipay.aop.api.domain.SignedCrossResult import SignedCrossResult


class AntlescenterFileDTO(object):

    def __init__(self):
        self._file_date = None
        self._file_hash = None
        self._file_id = None
        self._file_key = None
        self._file_md_5 = None
        self._file_name = None
        self._file_pages = None
        self._file_size = None
        self._file_url = None
        self._selected_seal_position_list = None
        self._signed_cross_results = None

    @property
    def file_date(self):
        return self._file_date

    @file_date.setter
    def file_date(self, value):
        self._file_date = value
    @property
    def file_hash(self):
        return self._file_hash

    @file_hash.setter
    def file_hash(self, value):
        self._file_hash = value
    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def file_key(self):
        return self._file_key

    @file_key.setter
    def file_key(self, value):
        self._file_key = value
    @property
    def file_md_5(self):
        return self._file_md_5

    @file_md_5.setter
    def file_md_5(self, value):
        self._file_md_5 = value
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value
    @property
    def file_pages(self):
        return self._file_pages

    @file_pages.setter
    def file_pages(self, value):
        self._file_pages = value
    @property
    def file_size(self):
        return self._file_size

    @file_size.setter
    def file_size(self, value):
        self._file_size = value
    @property
    def file_url(self):
        return self._file_url

    @file_url.setter
    def file_url(self, value):
        self._file_url = value
    @property
    def selected_seal_position_list(self):
        return self._selected_seal_position_list

    @selected_seal_position_list.setter
    def selected_seal_position_list(self, value):
        if isinstance(value, list):
            self._selected_seal_position_list = list()
            for i in value:
                if isinstance(i, SelectedSealPosition):
                    self._selected_seal_position_list.append(i)
                else:
                    self._selected_seal_position_list.append(SelectedSealPosition.from_alipay_dict(i))
    @property
    def signed_cross_results(self):
        return self._signed_cross_results

    @signed_cross_results.setter
    def signed_cross_results(self, value):
        if isinstance(value, list):
            self._signed_cross_results = list()
            for i in value:
                if isinstance(i, SignedCrossResult):
                    self._signed_cross_results.append(i)
                else:
                    self._signed_cross_results.append(SignedCrossResult.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.file_date:
            if hasattr(self.file_date, 'to_alipay_dict'):
                params['file_date'] = self.file_date.to_alipay_dict()
            else:
                params['file_date'] = self.file_date
        if self.file_hash:
            if hasattr(self.file_hash, 'to_alipay_dict'):
                params['file_hash'] = self.file_hash.to_alipay_dict()
            else:
                params['file_hash'] = self.file_hash
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
        if self.file_key:
            if hasattr(self.file_key, 'to_alipay_dict'):
                params['file_key'] = self.file_key.to_alipay_dict()
            else:
                params['file_key'] = self.file_key
        if self.file_md_5:
            if hasattr(self.file_md_5, 'to_alipay_dict'):
                params['file_md_5'] = self.file_md_5.to_alipay_dict()
            else:
                params['file_md_5'] = self.file_md_5
        if self.file_name:
            if hasattr(self.file_name, 'to_alipay_dict'):
                params['file_name'] = self.file_name.to_alipay_dict()
            else:
                params['file_name'] = self.file_name
        if self.file_pages:
            if hasattr(self.file_pages, 'to_alipay_dict'):
                params['file_pages'] = self.file_pages.to_alipay_dict()
            else:
                params['file_pages'] = self.file_pages
        if self.file_size:
            if hasattr(self.file_size, 'to_alipay_dict'):
                params['file_size'] = self.file_size.to_alipay_dict()
            else:
                params['file_size'] = self.file_size
        if self.file_url:
            if hasattr(self.file_url, 'to_alipay_dict'):
                params['file_url'] = self.file_url.to_alipay_dict()
            else:
                params['file_url'] = self.file_url
        if self.selected_seal_position_list:
            if isinstance(self.selected_seal_position_list, list):
                for i in range(0, len(self.selected_seal_position_list)):
                    element = self.selected_seal_position_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.selected_seal_position_list[i] = element.to_alipay_dict()
            if hasattr(self.selected_seal_position_list, 'to_alipay_dict'):
                params['selected_seal_position_list'] = self.selected_seal_position_list.to_alipay_dict()
            else:
                params['selected_seal_position_list'] = self.selected_seal_position_list
        if self.signed_cross_results:
            if isinstance(self.signed_cross_results, list):
                for i in range(0, len(self.signed_cross_results)):
                    element = self.signed_cross_results[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.signed_cross_results[i] = element.to_alipay_dict()
            if hasattr(self.signed_cross_results, 'to_alipay_dict'):
                params['signed_cross_results'] = self.signed_cross_results.to_alipay_dict()
            else:
                params['signed_cross_results'] = self.signed_cross_results
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntlescenterFileDTO()
        if 'file_date' in d:
            o.file_date = d['file_date']
        if 'file_hash' in d:
            o.file_hash = d['file_hash']
        if 'file_id' in d:
            o.file_id = d['file_id']
        if 'file_key' in d:
            o.file_key = d['file_key']
        if 'file_md_5' in d:
            o.file_md_5 = d['file_md_5']
        if 'file_name' in d:
            o.file_name = d['file_name']
        if 'file_pages' in d:
            o.file_pages = d['file_pages']
        if 'file_size' in d:
            o.file_size = d['file_size']
        if 'file_url' in d:
            o.file_url = d['file_url']
        if 'selected_seal_position_list' in d:
            o.selected_seal_position_list = d['selected_seal_position_list']
        if 'signed_cross_results' in d:
            o.signed_cross_results = d['signed_cross_results']
        return o


