<template>
    <div v-for="(item, index) in courses" class="pa-5">
        <Card :name="item.coursename" :card-colour="item.colour"/>
    </div>
</template>

<script lang="ts">

    import Card from './Card.vue';

    export default {
        components: {
            Card
        },
        props: {
            courses: {
                type: Array,
                required: true
            }
        }
    }

</script>