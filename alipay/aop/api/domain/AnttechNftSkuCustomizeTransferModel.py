#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechNftSkuCustomizeTransferModel(object):

    def __init__(self):
        self._camp_id = None
        self._fans_id = None
        self._fans_id_type = None
        self._sku_id = None
        self._source_file_id = None
        self._sticker_file_id = None
        self._third_biz_no = None
        self._thumbnail_file_id = None

    @property
    def camp_id(self):
        return self._camp_id

    @camp_id.setter
    def camp_id(self, value):
        self._camp_id = value
    @property
    def fans_id(self):
        return self._fans_id

    @fans_id.setter
    def fans_id(self, value):
        self._fans_id = value
    @property
    def fans_id_type(self):
        return self._fans_id_type

    @fans_id_type.setter
    def fans_id_type(self, value):
        self._fans_id_type = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def source_file_id(self):
        return self._source_file_id

    @source_file_id.setter
    def source_file_id(self, value):
        self._source_file_id = value
    @property
    def sticker_file_id(self):
        return self._sticker_file_id

    @sticker_file_id.setter
    def sticker_file_id(self, value):
        self._sticker_file_id = value
    @property
    def third_biz_no(self):
        return self._third_biz_no

    @third_biz_no.setter
    def third_biz_no(self, value):
        self._third_biz_no = value
    @property
    def thumbnail_file_id(self):
        return self._thumbnail_file_id

    @thumbnail_file_id.setter
    def thumbnail_file_id(self, value):
        self._thumbnail_file_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.camp_id:
            if hasattr(self.camp_id, 'to_alipay_dict'):
                params['camp_id'] = self.camp_id.to_alipay_dict()
            else:
                params['camp_id'] = self.camp_id
        if self.fans_id:
            if hasattr(self.fans_id, 'to_alipay_dict'):
                params['fans_id'] = self.fans_id.to_alipay_dict()
            else:
                params['fans_id'] = self.fans_id
        if self.fans_id_type:
            if hasattr(self.fans_id_type, 'to_alipay_dict'):
                params['fans_id_type'] = self.fans_id_type.to_alipay_dict()
            else:
                params['fans_id_type'] = self.fans_id_type
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.source_file_id:
            if hasattr(self.source_file_id, 'to_alipay_dict'):
                params['source_file_id'] = self.source_file_id.to_alipay_dict()
            else:
                params['source_file_id'] = self.source_file_id
        if self.sticker_file_id:
            if hasattr(self.sticker_file_id, 'to_alipay_dict'):
                params['sticker_file_id'] = self.sticker_file_id.to_alipay_dict()
            else:
                params['sticker_file_id'] = self.sticker_file_id
        if self.third_biz_no:
            if hasattr(self.third_biz_no, 'to_alipay_dict'):
                params['third_biz_no'] = self.third_biz_no.to_alipay_dict()
            else:
                params['third_biz_no'] = self.third_biz_no
        if self.thumbnail_file_id:
            if hasattr(self.thumbnail_file_id, 'to_alipay_dict'):
                params['thumbnail_file_id'] = self.thumbnail_file_id.to_alipay_dict()
            else:
                params['thumbnail_file_id'] = self.thumbnail_file_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechNftSkuCustomizeTransferModel()
        if 'camp_id' in d:
            o.camp_id = d['camp_id']
        if 'fans_id' in d:
            o.fans_id = d['fans_id']
        if 'fans_id_type' in d:
            o.fans_id_type = d['fans_id_type']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'source_file_id' in d:
            o.source_file_id = d['source_file_id']
        if 'sticker_file_id' in d:
            o.sticker_file_id = d['sticker_file_id']
        if 'third_biz_no' in d:
            o.third_biz_no = d['third_biz_no']
        if 'thumbnail_file_id' in d:
            o.thumbnail_file_id = d['thumbnail_file_id']
        return o


