<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>References</h1>
        <hr><br><br>
        <!--button type="button" class="btn btn-success btn-sm">Add Book</button-->
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">RepositoryID</th>
              <th scope="col">CommitID</th>
              <th scope="col">Kind</th>
              <th scope="col">SubKind</th>
              <th scope="col">Size (KiB)</th>
              <th scope="col">Collected At</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(reference, index) in references" :key="index">
              <td>{{ reference.repositoryId }}</td>
              <td>{{ reference.commitId }}</td>
              <td>{{ reference.kind }}</td>
              <td>{{ reference.subkind }}</td>
              <td>{{ reference.sizeKiB }}</td>
              <td>{{ reference.collectedAt }}</td>
              <!--td>
                <span v-if="reference.read">Yes</span>
                <span v-else>No</span>
              </td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-warning btn-sm">Update</button>
                  <button type="button" class="btn btn-danger btn-sm">Delete</button>
                </div>
              </td-->
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      references: [],
    };
  },
  methods: {
    getReferences() {
      const path = 'http://localhost:5000/api/v1/references';
      axios.get(path)
        .then((res) => {
          this.references = res.data.items;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getReferences();
  },
};
</script>
