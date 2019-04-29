package main

import (
	"fmt"
	"log"
	"os"
	"path/filepath"

	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/client-go/kubernetes"
	"k8s.io/client-go/tools/clientcmd"
)

func main() {
	kubeconfig := filepath.Join(os.Getenv("HOME"), ".kube", "config")
	log.Println("Using kubeconfig file: ", kubeconfig)
	config, err := clientcmd.BuildConfigFromFlags("", kubeconfig)
	if err != nil {
		log.Fatal(err)
	}

	clientset, err := kubernetes.NewForConfig(config)

	if err != nil {
		log.Fatal(err)
	}

	namespaces, err := clientset.CoreV1().Namespaces().List(metav1.ListOptions{})

	if err != nil {
		log.Fatalln("failed to get pods:", err)
	}

	for i, namespace := range namespaces.Items {
		log.Println("Iteration number: ", i)
		fmt.Println(namespace.GetName())
	}
}
