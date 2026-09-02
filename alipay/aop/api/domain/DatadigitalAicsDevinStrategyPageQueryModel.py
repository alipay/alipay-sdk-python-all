#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SearchField import SearchField
from alipay.aop.api.domain.SearchField import SearchField
from alipay.aop.api.domain.SortField import SortField


class DatadigitalAicsDevinStrategyPageQueryModel(object):

    def __init__(self):
        self._condition_join_type_enum = None
        self._crm_cue_open_enum = None
        self._crm_query_type_enum = None
        self._current = None
        self._form_code = None
        self._global_search_field_list = None
        self._has_followed = None
        self._must_exist_fields = None
        self._must_not_exist_fields = None
        self._need_mask_field = None
        self._new_data_format = None
        self._or_not_empty_fields = None
        self._owner = None
        self._page_size = None
        self._recall_field_list = None
        self._search_fields = None
        self._search_keyword = None
        self._search_should_fields = None
        self._sort_fields = None
        self._tenant_id = None

    @property
    def condition_join_type_enum(self):
        return self._condition_join_type_enum

    @condition_join_type_enum.setter
    def condition_join_type_enum(self, value):
        self._condition_join_type_enum = value
    @property
    def crm_cue_open_enum(self):
        return self._crm_cue_open_enum

    @crm_cue_open_enum.setter
    def crm_cue_open_enum(self, value):
        self._crm_cue_open_enum = value
    @property
    def crm_query_type_enum(self):
        return self._crm_query_type_enum

    @crm_query_type_enum.setter
    def crm_query_type_enum(self, value):
        self._crm_query_type_enum = value
    @property
    def current(self):
        return self._current

    @current.setter
    def current(self, value):
        self._current = value
    @property
    def form_code(self):
        return self._form_code

    @form_code.setter
    def form_code(self, value):
        self._form_code = value
    @property
    def global_search_field_list(self):
        return self._global_search_field_list

    @global_search_field_list.setter
    def global_search_field_list(self, value):
        if isinstance(value, list):
            self._global_search_field_list = list()
            for i in value:
                self._global_search_field_list.append(i)
    @property
    def has_followed(self):
        return self._has_followed

    @has_followed.setter
    def has_followed(self, value):
        self._has_followed = value
    @property
    def must_exist_fields(self):
        return self._must_exist_fields

    @must_exist_fields.setter
    def must_exist_fields(self, value):
        if isinstance(value, list):
            self._must_exist_fields = list()
            for i in value:
                self._must_exist_fields.append(i)
    @property
    def must_not_exist_fields(self):
        return self._must_not_exist_fields

    @must_not_exist_fields.setter
    def must_not_exist_fields(self, value):
        if isinstance(value, list):
            self._must_not_exist_fields = list()
            for i in value:
                self._must_not_exist_fields.append(i)
    @property
    def need_mask_field(self):
        return self._need_mask_field

    @need_mask_field.setter
    def need_mask_field(self, value):
        self._need_mask_field = value
    @property
    def new_data_format(self):
        return self._new_data_format

    @new_data_format.setter
    def new_data_format(self, value):
        self._new_data_format = value
    @property
    def or_not_empty_fields(self):
        return self._or_not_empty_fields

    @or_not_empty_fields.setter
    def or_not_empty_fields(self, value):
        if isinstance(value, list):
            self._or_not_empty_fields = list()
            for i in value:
                self._or_not_empty_fields.append(i)
    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def recall_field_list(self):
        return self._recall_field_list

    @recall_field_list.setter
    def recall_field_list(self, value):
        if isinstance(value, list):
            self._recall_field_list = list()
            for i in value:
                self._recall_field_list.append(i)
    @property
    def search_fields(self):
        return self._search_fields

    @search_fields.setter
    def search_fields(self, value):
        if isinstance(value, SearchField):
            self._search_fields = value
        else:
            self._search_fields = SearchField.from_alipay_dict(value)
    @property
    def search_keyword(self):
        return self._search_keyword

    @search_keyword.setter
    def search_keyword(self, value):
        self._search_keyword = value
    @property
    def search_should_fields(self):
        return self._search_should_fields

    @search_should_fields.setter
    def search_should_fields(self, value):
        if isinstance(value, SearchField):
            self._search_should_fields = value
        else:
            self._search_should_fields = SearchField.from_alipay_dict(value)
    @property
    def sort_fields(self):
        return self._sort_fields

    @sort_fields.setter
    def sort_fields(self, value):
        if isinstance(value, SortField):
            self._sort_fields = value
        else:
            self._sort_fields = SortField.from_alipay_dict(value)
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.condition_join_type_enum:
            if hasattr(self.condition_join_type_enum, 'to_alipay_dict'):
                params['condition_join_type_enum'] = self.condition_join_type_enum.to_alipay_dict()
            else:
                params['condition_join_type_enum'] = self.condition_join_type_enum
        if self.crm_cue_open_enum:
            if hasattr(self.crm_cue_open_enum, 'to_alipay_dict'):
                params['crm_cue_open_enum'] = self.crm_cue_open_enum.to_alipay_dict()
            else:
                params['crm_cue_open_enum'] = self.crm_cue_open_enum
        if self.crm_query_type_enum:
            if hasattr(self.crm_query_type_enum, 'to_alipay_dict'):
                params['crm_query_type_enum'] = self.crm_query_type_enum.to_alipay_dict()
            else:
                params['crm_query_type_enum'] = self.crm_query_type_enum
        if self.current:
            if hasattr(self.current, 'to_alipay_dict'):
                params['current'] = self.current.to_alipay_dict()
            else:
                params['current'] = self.current
        if self.form_code:
            if hasattr(self.form_code, 'to_alipay_dict'):
                params['form_code'] = self.form_code.to_alipay_dict()
            else:
                params['form_code'] = self.form_code
        if self.global_search_field_list:
            if isinstance(self.global_search_field_list, list):
                for i in range(0, len(self.global_search_field_list)):
                    element = self.global_search_field_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.global_search_field_list[i] = element.to_alipay_dict()
            if hasattr(self.global_search_field_list, 'to_alipay_dict'):
                params['global_search_field_list'] = self.global_search_field_list.to_alipay_dict()
            else:
                params['global_search_field_list'] = self.global_search_field_list
        if self.has_followed:
            if hasattr(self.has_followed, 'to_alipay_dict'):
                params['has_followed'] = self.has_followed.to_alipay_dict()
            else:
                params['has_followed'] = self.has_followed
        if self.must_exist_fields:
            if isinstance(self.must_exist_fields, list):
                for i in range(0, len(self.must_exist_fields)):
                    element = self.must_exist_fields[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.must_exist_fields[i] = element.to_alipay_dict()
            if hasattr(self.must_exist_fields, 'to_alipay_dict'):
                params['must_exist_fields'] = self.must_exist_fields.to_alipay_dict()
            else:
                params['must_exist_fields'] = self.must_exist_fields
        if self.must_not_exist_fields:
            if isinstance(self.must_not_exist_fields, list):
                for i in range(0, len(self.must_not_exist_fields)):
                    element = self.must_not_exist_fields[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.must_not_exist_fields[i] = element.to_alipay_dict()
            if hasattr(self.must_not_exist_fields, 'to_alipay_dict'):
                params['must_not_exist_fields'] = self.must_not_exist_fields.to_alipay_dict()
            else:
                params['must_not_exist_fields'] = self.must_not_exist_fields
        if self.need_mask_field:
            if hasattr(self.need_mask_field, 'to_alipay_dict'):
                params['need_mask_field'] = self.need_mask_field.to_alipay_dict()
            else:
                params['need_mask_field'] = self.need_mask_field
        if self.new_data_format:
            if hasattr(self.new_data_format, 'to_alipay_dict'):
                params['new_data_format'] = self.new_data_format.to_alipay_dict()
            else:
                params['new_data_format'] = self.new_data_format
        if self.or_not_empty_fields:
            if isinstance(self.or_not_empty_fields, list):
                for i in range(0, len(self.or_not_empty_fields)):
                    element = self.or_not_empty_fields[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.or_not_empty_fields[i] = element.to_alipay_dict()
            if hasattr(self.or_not_empty_fields, 'to_alipay_dict'):
                params['or_not_empty_fields'] = self.or_not_empty_fields.to_alipay_dict()
            else:
                params['or_not_empty_fields'] = self.or_not_empty_fields
        if self.owner:
            if hasattr(self.owner, 'to_alipay_dict'):
                params['owner'] = self.owner.to_alipay_dict()
            else:
                params['owner'] = self.owner
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.recall_field_list:
            if isinstance(self.recall_field_list, list):
                for i in range(0, len(self.recall_field_list)):
                    element = self.recall_field_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.recall_field_list[i] = element.to_alipay_dict()
            if hasattr(self.recall_field_list, 'to_alipay_dict'):
                params['recall_field_list'] = self.recall_field_list.to_alipay_dict()
            else:
                params['recall_field_list'] = self.recall_field_list
        if self.search_fields:
            if hasattr(self.search_fields, 'to_alipay_dict'):
                params['search_fields'] = self.search_fields.to_alipay_dict()
            else:
                params['search_fields'] = self.search_fields
        if self.search_keyword:
            if hasattr(self.search_keyword, 'to_alipay_dict'):
                params['search_keyword'] = self.search_keyword.to_alipay_dict()
            else:
                params['search_keyword'] = self.search_keyword
        if self.search_should_fields:
            if hasattr(self.search_should_fields, 'to_alipay_dict'):
                params['search_should_fields'] = self.search_should_fields.to_alipay_dict()
            else:
                params['search_should_fields'] = self.search_should_fields
        if self.sort_fields:
            if hasattr(self.sort_fields, 'to_alipay_dict'):
                params['sort_fields'] = self.sort_fields.to_alipay_dict()
            else:
                params['sort_fields'] = self.sort_fields
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalAicsDevinStrategyPageQueryModel()
        if 'condition_join_type_enum' in d:
            o.condition_join_type_enum = d['condition_join_type_enum']
        if 'crm_cue_open_enum' in d:
            o.crm_cue_open_enum = d['crm_cue_open_enum']
        if 'crm_query_type_enum' in d:
            o.crm_query_type_enum = d['crm_query_type_enum']
        if 'current' in d:
            o.current = d['current']
        if 'form_code' in d:
            o.form_code = d['form_code']
        if 'global_search_field_list' in d:
            o.global_search_field_list = d['global_search_field_list']
        if 'has_followed' in d:
            o.has_followed = d['has_followed']
        if 'must_exist_fields' in d:
            o.must_exist_fields = d['must_exist_fields']
        if 'must_not_exist_fields' in d:
            o.must_not_exist_fields = d['must_not_exist_fields']
        if 'need_mask_field' in d:
            o.need_mask_field = d['need_mask_field']
        if 'new_data_format' in d:
            o.new_data_format = d['new_data_format']
        if 'or_not_empty_fields' in d:
            o.or_not_empty_fields = d['or_not_empty_fields']
        if 'owner' in d:
            o.owner = d['owner']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'recall_field_list' in d:
            o.recall_field_list = d['recall_field_list']
        if 'search_fields' in d:
            o.search_fields = d['search_fields']
        if 'search_keyword' in d:
            o.search_keyword = d['search_keyword']
        if 'search_should_fields' in d:
            o.search_should_fields = d['search_should_fields']
        if 'sort_fields' in d:
            o.sort_fields = d['sort_fields']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        return o


