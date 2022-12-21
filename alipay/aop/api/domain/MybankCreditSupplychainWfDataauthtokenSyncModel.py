#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditSupplychainWfDataauthtokenSyncModel(object):

    def __init__(self):
        self._change_date = None
        self._collection_status = None
        self._data_collection_info_ids = None
        self._platform_type = None
        self._requestid = None
        self._sellerid = None
        self._site = None
        self._siteuserid = None
        self._stopped_reason = None

    @property
    def change_date(self):
        return self._change_date

    @change_date.setter
    def change_date(self, value):
        self._change_date = value
    @property
    def collection_status(self):
        return self._collection_status

    @collection_status.setter
    def collection_status(self, value):
        self._collection_status = value
    @property
    def data_collection_info_ids(self):
        return self._data_collection_info_ids

    @data_collection_info_ids.setter
    def data_collection_info_ids(self, value):
        if isinstance(value, list):
            self._data_collection_info_ids = list()
            for i in value:
                self._data_collection_info_ids.append(i)
    @property
    def platform_type(self):
        return self._platform_type

    @platform_type.setter
    def platform_type(self, value):
        self._platform_type = value
    @property
    def requestid(self):
        return self._requestid

    @requestid.setter
    def requestid(self, value):
        self._requestid = value
    @property
    def sellerid(self):
        return self._sellerid

    @sellerid.setter
    def sellerid(self, value):
        self._sellerid = value
    @property
    def site(self):
        return self._site

    @site.setter
    def site(self, value):
        self._site = value
    @property
    def siteuserid(self):
        return self._siteuserid

    @siteuserid.setter
    def siteuserid(self, value):
        self._siteuserid = value
    @property
    def stopped_reason(self):
        return self._stopped_reason

    @stopped_reason.setter
    def stopped_reason(self, value):
        self._stopped_reason = value


    def to_alipay_dict(self):
        params = dict()
        if self.change_date:
            if hasattr(self.change_date, 'to_alipay_dict'):
                params['change_date'] = self.change_date.to_alipay_dict()
            else:
                params['change_date'] = self.change_date
        if self.collection_status:
            if hasattr(self.collection_status, 'to_alipay_dict'):
                params['collection_status'] = self.collection_status.to_alipay_dict()
            else:
                params['collection_status'] = self.collection_status
        if self.data_collection_info_ids:
            if isinstance(self.data_collection_info_ids, list):
                for i in range(0, len(self.data_collection_info_ids)):
                    element = self.data_collection_info_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.data_collection_info_ids[i] = element.to_alipay_dict()
            if hasattr(self.data_collection_info_ids, 'to_alipay_dict'):
                params['data_collection_info_ids'] = self.data_collection_info_ids.to_alipay_dict()
            else:
                params['data_collection_info_ids'] = self.data_collection_info_ids
        if self.platform_type:
            if hasattr(self.platform_type, 'to_alipay_dict'):
                params['platform_type'] = self.platform_type.to_alipay_dict()
            else:
                params['platform_type'] = self.platform_type
        if self.requestid:
            if hasattr(self.requestid, 'to_alipay_dict'):
                params['requestid'] = self.requestid.to_alipay_dict()
            else:
                params['requestid'] = self.requestid
        if self.sellerid:
            if hasattr(self.sellerid, 'to_alipay_dict'):
                params['sellerid'] = self.sellerid.to_alipay_dict()
            else:
                params['sellerid'] = self.sellerid
        if self.site:
            if hasattr(self.site, 'to_alipay_dict'):
                params['site'] = self.site.to_alipay_dict()
            else:
                params['site'] = self.site
        if self.siteuserid:
            if hasattr(self.siteuserid, 'to_alipay_dict'):
                params['siteuserid'] = self.siteuserid.to_alipay_dict()
            else:
                params['siteuserid'] = self.siteuserid
        if self.stopped_reason:
            if hasattr(self.stopped_reason, 'to_alipay_dict'):
                params['stopped_reason'] = self.stopped_reason.to_alipay_dict()
            else:
                params['stopped_reason'] = self.stopped_reason
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditSupplychainWfDataauthtokenSyncModel()
        if 'change_date' in d:
            o.change_date = d['change_date']
        if 'collection_status' in d:
            o.collection_status = d['collection_status']
        if 'data_collection_info_ids' in d:
            o.data_collection_info_ids = d['data_collection_info_ids']
        if 'platform_type' in d:
            o.platform_type = d['platform_type']
        if 'requestid' in d:
            o.requestid = d['requestid']
        if 'sellerid' in d:
            o.sellerid = d['sellerid']
        if 'site' in d:
            o.site = d['site']
        if 'siteuserid' in d:
            o.siteuserid = d['siteuserid']
        if 'stopped_reason' in d:
            o.stopped_reason = d['stopped_reason']
        return o


