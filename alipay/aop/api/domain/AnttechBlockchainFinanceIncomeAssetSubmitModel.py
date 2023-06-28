#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RelatedParties import RelatedParties


class AnttechBlockchainFinanceIncomeAssetSubmitModel(object):

    def __init__(self):
        self._asset_out_no = None
        self._biz_no = None
        self._device_type = None
        self._distribution_pro_no = None
        self._material_brand = None
        self._material_model_no = None
        self._produce_date = None
        self._prove_file_id = None
        self._related_parties = None

    @property
    def asset_out_no(self):
        return self._asset_out_no

    @asset_out_no.setter
    def asset_out_no(self, value):
        self._asset_out_no = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        self._device_type = value
    @property
    def distribution_pro_no(self):
        return self._distribution_pro_no

    @distribution_pro_no.setter
    def distribution_pro_no(self, value):
        self._distribution_pro_no = value
    @property
    def material_brand(self):
        return self._material_brand

    @material_brand.setter
    def material_brand(self, value):
        self._material_brand = value
    @property
    def material_model_no(self):
        return self._material_model_no

    @material_model_no.setter
    def material_model_no(self, value):
        self._material_model_no = value
    @property
    def produce_date(self):
        return self._produce_date

    @produce_date.setter
    def produce_date(self, value):
        self._produce_date = value
    @property
    def prove_file_id(self):
        return self._prove_file_id

    @prove_file_id.setter
    def prove_file_id(self, value):
        self._prove_file_id = value
    @property
    def related_parties(self):
        return self._related_parties

    @related_parties.setter
    def related_parties(self, value):
        if isinstance(value, list):
            self._related_parties = list()
            for i in value:
                if isinstance(i, RelatedParties):
                    self._related_parties.append(i)
                else:
                    self._related_parties.append(RelatedParties.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.asset_out_no:
            if hasattr(self.asset_out_no, 'to_alipay_dict'):
                params['asset_out_no'] = self.asset_out_no.to_alipay_dict()
            else:
                params['asset_out_no'] = self.asset_out_no
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.device_type:
            if hasattr(self.device_type, 'to_alipay_dict'):
                params['device_type'] = self.device_type.to_alipay_dict()
            else:
                params['device_type'] = self.device_type
        if self.distribution_pro_no:
            if hasattr(self.distribution_pro_no, 'to_alipay_dict'):
                params['distribution_pro_no'] = self.distribution_pro_no.to_alipay_dict()
            else:
                params['distribution_pro_no'] = self.distribution_pro_no
        if self.material_brand:
            if hasattr(self.material_brand, 'to_alipay_dict'):
                params['material_brand'] = self.material_brand.to_alipay_dict()
            else:
                params['material_brand'] = self.material_brand
        if self.material_model_no:
            if hasattr(self.material_model_no, 'to_alipay_dict'):
                params['material_model_no'] = self.material_model_no.to_alipay_dict()
            else:
                params['material_model_no'] = self.material_model_no
        if self.produce_date:
            if hasattr(self.produce_date, 'to_alipay_dict'):
                params['produce_date'] = self.produce_date.to_alipay_dict()
            else:
                params['produce_date'] = self.produce_date
        if self.prove_file_id:
            if hasattr(self.prove_file_id, 'to_alipay_dict'):
                params['prove_file_id'] = self.prove_file_id.to_alipay_dict()
            else:
                params['prove_file_id'] = self.prove_file_id
        if self.related_parties:
            if isinstance(self.related_parties, list):
                for i in range(0, len(self.related_parties)):
                    element = self.related_parties[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.related_parties[i] = element.to_alipay_dict()
            if hasattr(self.related_parties, 'to_alipay_dict'):
                params['related_parties'] = self.related_parties.to_alipay_dict()
            else:
                params['related_parties'] = self.related_parties
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceIncomeAssetSubmitModel()
        if 'asset_out_no' in d:
            o.asset_out_no = d['asset_out_no']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'device_type' in d:
            o.device_type = d['device_type']
        if 'distribution_pro_no' in d:
            o.distribution_pro_no = d['distribution_pro_no']
        if 'material_brand' in d:
            o.material_brand = d['material_brand']
        if 'material_model_no' in d:
            o.material_model_no = d['material_model_no']
        if 'produce_date' in d:
            o.produce_date = d['produce_date']
        if 'prove_file_id' in d:
            o.prove_file_id = d['prove_file_id']
        if 'related_parties' in d:
            o.related_parties = d['related_parties']
        return o


